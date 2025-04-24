from flask import Flask
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Configure the app
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')
    app.config['OPENWEATHER_API_KEY'] = os.environ.get('OPENWEATHER_API_KEY')
    
    # Register blueprints
    from .routes import main
    app.register_blueprint(main)
    
    return app 