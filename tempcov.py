from flask import Flask, render_template, request

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        choice = request.form['choice']
        temperature = float(request.form['temperature'])

        if choice == 'celsius_to_fahrenheit':
            result = celsius_to_fahrenheit(temperature)
            units = "°F"
        else:
            result = fahrenheit_to_celsius(temperature)
            units = "°C"

        return render_template('tempcov.html', result=result, units=units)

    return render_template('tempcov.html')

if __name__ == '__main__':
    app.run(debug=True)
