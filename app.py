# app.py
from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression', '')
    
    try:
        # Replace some JS math functions with Python equivalents
        expression = expression.replace('Math.PI', 'math.pi')
        expression = expression.replace('Math.E', 'math.e')
        expression = expression.replace('Math.sqrt', 'math.sqrt')
        expression = expression.replace('Math.sin', 'math.sin')
        expression = expression.replace('Math.cos', 'math.cos')
        expression = expression.replace('Math.tan', 'math.tan')
        expression = expression.replace('Math.log', 'math.log10')
        expression = expression.replace('Math.ln', 'math.log')
        expression = expression.replace('Math.pow', 'math.pow')
        expression = expression.replace('Math.exp', 'math.exp')
        
        # Evaluate the expression safely
        result = eval(expression, {'__builtins__': None}, {'math': math})
        
        return jsonify({'result': result, 'error': None})
    except Exception as e:
        return jsonify({'result': None, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)