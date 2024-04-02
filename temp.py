from flask import Flask, render_template, request

app = Flask(__name__)

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        calculator = Calculator()
        a = float(request.form.get('a'))
        b = float(request.form.get('b'))
        operation = request.form.get('operation')

        if operation == 'add':
            result = calculator.add(a, b)
        elif operation == 'subtract':
            result = calculator.subtract(a, b)
        elif operation == 'multiply':
            result = calculator.multiply(a, b)
        elif operation == 'divide':
            result = calculator.divide(a, b)

    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)