import requests

from flask import Flask, render_template, request
from helpers import from_fahrenheit_to_celsius

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        city = request.form.get('city')
        measure = request.form.get('measure')
    else:
        city = 'New York'
        measure = 'C'

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&id=524901&appid=f7d2087ab3d7b45f500f122b9fd27c19'

    data = requests.get(url.format(city)).json()

    if measure == 'C':
        temperature = from_fahrenheit_to_celsius(data['main']['temp'])
    else:
        temperature = int(data['main']['temp'])

    weather = {
        'city': city,
        'temperature': temperature,
        'measure': measure,
        'description': data['weather'][0]['description'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed'],
        'icon': data['weather'][0]['icon'],
    }

    return render_template('base.html', weather=weather)


if __name__ == '__main__':
    app.run(debug=True)