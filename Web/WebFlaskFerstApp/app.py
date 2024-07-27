from flask import Flask, render_template, request, redirect
from static.logic.logic import convert_to_fahrenheit, convert_to_kelvin, calculate_bmi
from form import Form


app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/temperature', methods=["POST", "GET"])
def temperature_converter():
    if request.method == 'POST':

        if 'Fahrenheit' in request.form.keys():

            temperature = convert_to_fahrenheit(request.form['temperature'])

            return render_template('/resultTemperature.html', newtemperature=temperature, scale="Фаренгейту")

        if 'Kelvin' in request.form.keys():

            temperature = convert_to_kelvin(request.form['temperature'])

            return render_template('/resultTemperature.html', newtemperature=temperature, scale="Кельвину")

    else:
        return render_template('temperature.html')


@app.route('/bmi', methods=["POST", "GET"])
def calc_bmi():
    if request.method == 'POST':

        weight = request.form['weight']
        height = request.form['height']

        bmi = calculate_bmi(weight, height)

        return render_template('/resultBMI.html', bmi=bmi)

    else:
        return render_template('bmi.html')


@app.route('/toDo')
def to_do():
    return render_template('toDo.html')


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "GET":
        form = Form()
        return render_template('register.html', form=form)
    # else:
    #     form = Form()
    #     if form.validate_on_submit():
    #         return render_template('register.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)