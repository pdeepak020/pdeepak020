# Weather Forecast Web Application

A simple web application that provides current weather and 5-day forecast for any city using the OpenWeather API.

## Features

- Search for weather by city name
- Display current weather conditions
- Show 5-day forecast with 3-hour intervals
- Responsive design for mobile and desktop
- Error handling for API requests

## Prerequisites

- Python 3.8 or higher
- OpenWeather API key (get one for free at [OpenWeather](https://openweathermap.org/api))

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd weatherforecast
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with your API key:
   ```
   SECRET_KEY=your-secret-key-here
   OPENWEATHER_API_KEY=your-openweather-api-key-here
   ```

## Running the Application

1. Make sure your virtual environment is activated.

2. Run the application:
   ```
   python run.py
   ```

3. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Usage

1. Enter a city name in the search box (e.g., London, New York, Tokyo)
2. Click the Search button
3. View the current weather and 5-day forecast

## Project Structure

```
weatherforecast/
├── app/
│   ├── static/
│   │   └── style.css
│   ├── templates/
│   │   ├── base.html
│   │   └── index.html
│   ├── __init__.py
│   └── routes.py
├── .env
├── requirements.txt
├── README.md
└── run.py
```

## Technologies Used

- Flask - Web framework
- Requests - HTTP library for API calls
- Bootstrap 5 - CSS framework
- Font Awesome - Icons
- OpenWeather API - Weather data

## License

This project is licensed under the MIT License - see the LICENSE file for details. 