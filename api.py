import json
from flask import Blueprint, jsonify, request
import os
from dotenv import load_dotenv
from google import genai
from calculations.calculations import CALC_REGISTRY

bp = Blueprint("api", __name__, url_prefix="/api")

DATA_PATH = "data/calculations.json"
VERSION_PATH = "data/metadata_version.txt"

load_dotenv()

GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

def load_metadata():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def load_version():
    if os.path.exists(VERSION_PATH):
        return open(VERSION_PATH).read().strip()
    return "0.0.0"   


@bp.route("/metadata/version", methods=["GET"])
def metadata_version():
    return jsonify({"version": load_version()})


@bp.route("/metadata", methods=["GET"])
def metadata():
    data = load_metadata()
    return jsonify({
        "version": load_version(),
        "data": data
    })
    

@bp.route("/compute", methods=["POST"])
def compute():
    """
    Expected JSON:
    {
        "name": "Body Mass Index (BMI)",
        "params": { "weight": 80, "height": 1.85 }
    }
    """

    payload = request.json or {}
    name = payload.get("name")  
    params = payload.get("params", {})

    if not name:
        return jsonify({"error": "name is required"}), 400

    data = load_metadata()
    calculation = None

    for cat in data.get("categories", []):
        for calc in cat.get("calculations", []):
            if calc.get("name") == name:  
                calculation = calc
                break
        if calculation:
            break

    if not calculation:
        return jsonify({"error": f"calculation '{name}' not found"}), 404

    calc_name = calculation["name"]

    func = CALC_REGISTRY.get(calc_name)
    if not func:
        return jsonify({"error": f"no backend implementation for '{calc_name}'"}), 500

    try:
        ordered_args = []
        for p in calculation.get("parameters", []):
            pname = p["name"]

            if pname not in params:
                return jsonify({"error": f"missing parameter: {pname}"}), 400

            value = params[pname]

            if p["type"] == "float":
                value = float(value)
            elif p["type"] == "integer":
                value = int(value)
            elif p["type"] == "string":
                value = str(value)

            if p.get("enum") and value not in p["enum"]:
                return jsonify({"error": f"invalid value for {pname}. Allowed: {p['enum']}"}), 400

            ordered_args.append(value)

    except Exception as e:
        return jsonify({"error": f"parameter processing error: {str(e)}"}), 400

    try:
        result = func(*ordered_args)
    except Exception as e:
        return jsonify({"error": "calculation execution error", "details": str(e)}), 500

    return jsonify({
        "name": calc_name,
        "result": result,
        "unit": calculation.get("result_unit")
    })

@bp.route("/explain", methods=["POST"])
def explain():
    """
    Expected JSON:
    {
        "calc_name": "Body Mass Index (BMI)",
        "result": 24.5,
        "parameters": { "weight": 80, "height": 1.85, "age": 35, "sex": "male" },
        "additional_context": "Patient has diabetes"
    }
    """
    req_data = request.json or {}
    calc_name = req_data.get('calc_name')
    result = req_data.get('result')
    parameters = req_data.get('parameters', {})
    additional_context = req_data.get('additional_context', '')

    if not calc_name or result is None:
        return jsonify({"error": "calc_name and result are required"}), 400

    def extract_param(keys):
        for key in keys:
            for param_key in parameters:
                if param_key.lower() == key:
                    return parameters[param_key]
        return ''

    age = extract_param(['age'])
    sex = extract_param(['sex', 'gender'])
    race = extract_param(['race', 'ethnicity'])

    for key in list(parameters.keys()):
        if key.lower() in ['age', 'sex', 'gender', 'race', 'ethnicity']:
            parameters.pop(key)

    age_str = f"\nPatient Age: {age}" if age else ""
    sex_str = f"\nPatient Sex: {sex}" if sex else ""
    race_str = f"\nPatient Race: {race}" if race else ""
    context_str = f"\nAdditional Context: {additional_context}" if additional_context else ""

    data = load_metadata()
    unit = ""
    for category in data['categories']:
        for calc in category.get('calculations', []):
            if calc['name'] == calc_name:
                unit = calc.get('result_unit', '') or ''
                break
    
    param_str = ""
    if parameters:
        param_str = "\nCalculation Parameters:\n" + "\n".join(
            f"- {k}: {v}" for k, v in parameters.items()
        )

    prompt = f"""You are a senior clinical nursing assistant AI. When I provide you a lab value or a medical calculation result, you will:
  1) State whether the result is within the normal reference range (or above/below),
  2) Explain what an abnormal value could imply about the patient's condition,
  3) List any potential nursing concerns or next steps.
  4) Use plain language—suitable for a registered nurse (RN),
  5) Keep your answer to 3–5 bullet points.

Calculation Name: {calc_name}
Result Value: {result} {unit}
Unit: {unit}
{age_str}{sex_str}{race_str}{context_str}
{param_str}

Please provide your explanation now:"""
    
    if not GEMINI_API_KEY:
        return jsonify({"error": "GEMINI_API_KEY not configured"}), 500

    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        return jsonify({"explanation": response.text})
            
    except Exception as e:
        print("Gemini error:", e)
        return jsonify({"error": "Sorry, could not get explanation.", "details": str(e)}), 500


@bp.route("/chat", methods=["POST"])
def chat():
    """
    Expected JSON:
    {
        "message": "What is BMI?",
        "context": "System context with recents and favorites",
        "recents": [...],
        "favorites": [...]
    }
    """
    req_data = request.json or {}
    user_message = req_data.get('message', '')
    system_context = req_data.get('context', '')
    recents = req_data.get('recents', [])
    favorites = req_data.get('favorites', [])

    if not user_message:
        return jsonify({"error": "message is required"}), 400

    if not GEMINI_API_KEY:
        return jsonify({"error": "GEMINI_API_KEY not configured"}), 500

    recents_info = ""
    if recents:
        recents_lines = []
        for r in recents[:5]:
            name = r.get('calculationName', 'Unknown Calculation')
            result = r.get('result', 'N/A')
            unit = r.get('unit', '')
            recents_lines.append(f"- {name}: {result} {unit}")
        if recents_lines:
            recents_info = "\n\nRecent Calculations:\n" + "\n".join(recents_lines)

    favorites_info = ""
    if favorites:
        favorites_lines = []
        for f in favorites:
            name = f.get('calculationName', 'Unknown Calculator')
            favorites_lines.append(f"- {name}")
        if favorites_lines:
            favorites_info = "\n\nFavorite Calculators:\n" + "\n".join(favorites_lines)

    system_prompt = f"""You are ClinicalC AI Assistant, helping healthcare professionals with medical calculations.

{system_context}
{recents_info}
{favorites_info}

Guidelines:
1. Be concise and clinical (2-4 short paragraphs max)
2. Only suggest opening a calculator when specifically relevant to the question
3. When suggesting a calculator, use this EXACT format with the actual slug value: [CALCULATOR:body-mass-index:Body Mass Index]
   Example: If user asks about BMI, respond with [CALCULATOR:body-mass-index:Body Mass Index (BMI)]
   IMPORTANT: Use the actual slug from the Available Calculators list, not the word "slug"
4. Use plain text formatting - NO asterisks, NO markdown, NO special formatting
5. Reference user's recents/favorites when relevant
6. Respond warmly to greetings (hello, hi, how are you, thanks, etc.) in a friendly but professional manner e.g "Hello! I'm CLINICALC's AI Assistant. How can I assist you with medical calculations today?"
7. IMPORTANT: Only answer questions related to medical calculations, clinical scores, medical formulas, unit conversions, or healthcare topics
8. If asked about unrelated topics, politely decline with: "I can only assist with medical-related questions and calculations. Is there a clinical calculator or medical formula I can help you with?"
CRITICAL: You MUST end EVERY response with 3 follow-up questions in this EXACT format on a new line:
[SUGGESTIONS:What would you like to calculate?|Show me my recent calculations|How is this score interpreted?]

Example response:
"The BMI calculator measures body mass index based on height and weight. [CALCULATOR:body-mass-index:Body Mass Index (BMI)]

[SUGGESTIONS:What's a healthy BMI range?|Show my recent calculations|Calculate my BMR?]"

Keep responses under 200 words. NEVER forget the [SUGGESTIONS:...] line."""

    full_prompt = f"{system_prompt}\n\nUser: {user_message}\n\nAssistant:"

    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=full_prompt
        )
        
        return jsonify({"response": response.text})
            
    except Exception as e:
        print("Gemini chat error:", e)
        return jsonify({
            "error": "Could not process chat request",
            "details": str(e)
        }), 500