from dotenv import load_dotenv
import os
import requests
import logging
from flask import Flask
from waitress import serve

app = Flask(__name__)
logger = logging.getLogger('waitress')
logger.setLevel(logging.DEBUG)

load_dotenv()
LASTFM_API_KEY = os.environ.get('LASTFM_API_KEY')
OPENWEATHERMAP_API_KEY = os.environ.get('OPENWEATHERMAP_API_KEY')


@app.route('/')
def main_page():
    return ':)'


@app.route('/lastfm/<string:username>')
def get_now_playing_track(username):
    url = f'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={username}&api_key={LASTFM_API_KEY}&format=json&limit=1'
    response = requests.get(url)
    data = response.json()

    try:
        track_info = data['recenttracks']['track'][0]
        if '@attr' in track_info and track_info['@attr']['nowplaying'] == 'true':
            track = track_info['name']
            artist = track_info['artist']['#text']
            return f'{artist} - {track}'
        else:
            return f'Сейчас ничего не скробблится'
    except:
        return f'Ошибка получения данных'


@app.route('/weather/<string:city>')
def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}&units=metric&lang=ru'
    response = requests.get(url)
    data = response.json()

    if 'weather' in data and 'main' in data:
        weather_description = data['weather'][0]['description']
        temp = data['main']['temp']
        temp_feel = data['main']['feels_like']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        wind_degree = data['wind']['deg']

        directions = ['С', 'СВ', 'В', 'ЮВ', 'Ю', 'ЮЗ', 'З', 'СЗ']
        wind_direction = directions[round(wind_degree / (360. / len(directions))) % len(directions)]

        return f'{city} - сейчас {weather_description}. Температура - {round(temp)}°C (по ощущению {round(temp_feel)}°C). Ветер - {wind_direction}, {wind_speed} м/с. Влажность - {humidity}%, давление ~{round(pressure/1.333, 1)} мм рт.ст.'
    else:
        return f'{city} - не получилось узнать погоду :('


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port='8080')
    # app.run(host='0.0.0.0', port=6789, debug=True)
