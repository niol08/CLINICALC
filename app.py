from flask import Flask, render_template, url_for, request, jsonify
import json
import os
import calculations

app = Flask(__name__) 

app.config['TEMPLATES_AUTO_RELOAD'] = True

#Load the JSON file
json_path = os.path.join(app.root_path, 'data', 'calculations.json')
with open(json_path, encoding='utf-8') as f:
    data = json.load(f)

def execute_function(function_name, parameters):
    try:
        # Get the function from the calculations module
        function = getattr(calculations, function_name)
        # Create a dictionary of parameters
        param_dict = {param: float(request.form[param]) for param in parameters}
        # Execute the function
        result = function(**param_dict)
        return result
    except Exception as e:
        return str(e)



@app.route('/')
def index():
    cards = data['categories']
    return render_template('index.html', cards=cards)

   
@app.route('/card/<slug>', methods=['GET', 'POST'])
def card_detail(slug):
    card = next((card for card in data['categories'] if card["slug"] == slug), None)
    if card is None:
        return "Card not found", 404
    if request.method == 'POST':
        calculation_name = request.form['calculation_name']
        calculation = next((calc for calc in card['calculations'] if calc['name'] == calculation_name), None)
        if calculation:
            result = execute_function(calculation['function'], calculation['parameters'])
            return jsonify(result=result)

    return render_template('card_detail.html', card=card)
   
if __name__ == '__main__':
    app.run(debug=True)