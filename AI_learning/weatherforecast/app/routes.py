from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
import requests
import json
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error = None
    
    if request.method == 'POST':
        city = request.form.get('city')
        
        if not city:
            flash('Please enter a city name', 'error')
            return redirect(url_for('main.index'))
        
        # Get API key from config
        api_key = current_app.config.get('OPENWEATHER_API_KEY')
        
        if not api_key:
            flash('OpenWeather API key is not configured', 'error')
            return redirect(url_for('main.index'))
        
        # Make API request to OpenWeather
        try:
            # Get current weather
            current_weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            current_response = requests.get(current_weather_url)
            current_data = current_response.json()
            
            if current_response.status_code != 200:
                flash(f"Error: {current_data.get('message', 'Unknown error')}", 'error')
                return redirect(url_for('main.index'))
            
            # Get 5-day forecast
            forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
            forecast_response = requests.get(forecast_url)
            forecast_data = forecast_response.json()
            
            if forecast_response.status_code != 200:
                flash(f"Error: {forecast_data.get('message', 'Unknown error')}", 'error')
                return redirect(url_for('main.index'))
            
            # Process the data
            weather_data = {
                'city': current_data['name'],
                'country': current_data['sys']['country'],
                'current': {
                    'temp': round(current_data['main']['temp']),
                    'feels_like': round(current_data['main']['feels_like']),
                    'humidity': current_data['main']['humidity'],
                    'wind_speed': current_data['wind']['speed'],
                    'description': current_data['weather'][0]['description'],
                    'icon': current_data['weather'][0]['icon'],
                    'time': datetime.fromtimestamp(current_data['dt']).strftime('%Y-%m-%d %H:%M')
                },
                'forecast': []
            }
            
            # Process 5-day forecast (every 3 hours)
            for item in forecast_data['list']:
                forecast_item = {
                    'time': datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d %H:%M'),
                    'temp': round(item['main']['temp']),
                    'description': item['weather'][0]['description'],
                    'icon': item['weather'][0]['icon']
                }
                weather_data['forecast'].append(forecast_item)
            
        except requests.exceptions.RequestException as e:
            flash(f"Error connecting to weather service: {str(e)}", 'error')
            return redirect(url_for('main.index'))
        except (KeyError, json.JSONDecodeError) as e:
            flash(f"Error processing weather data: {str(e)}", 'error')
            return redirect(url_for('main.index'))
    
    return render_template('index.html', weather_data=weather_data) 