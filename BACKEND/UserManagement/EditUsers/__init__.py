from flask import Flask
from database import configure_database
from routes import init_routes

def create_app():
    app = Flask(__name__)
    
 # Configure the database
    configure_database(app)
    
    # Register the routes
    init_routes(app)
    
    return app
