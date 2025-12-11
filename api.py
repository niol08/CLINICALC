
import json
from flask import Blueprint, jsonify, request
import os
from calculations.calculations import CALC_REGISTRY

bp = Blueprint("api", __name__, url_prefix="/api")

DATA_PATH = "data/calculations.json"
VERSION_PATH = "data/metadata_version.txt"

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
    name = payload.get("name")  # Changed from slug to name
    params = payload.get("params", {})

    if not name:
        return jsonify({"error": "name is required"}), 400

    data = load_metadata()
    calculation = None

    for cat in data.get("categories", []):
        for calc in cat.get("calculations", []):
            if calc.get("name") == name:  # Match by name instead of slug
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

