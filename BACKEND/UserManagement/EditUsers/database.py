from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def configure_database(app):
    """
    Configures the database for the Flask application using SQLAlchemy.
    The database URI is loaded from the 'DATABASE_URL' environment variable.
    """
    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        raise ValueError("DATABASE_URL is not configured in the environment variables")

    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable to improve performance
    db.init_app(app)
