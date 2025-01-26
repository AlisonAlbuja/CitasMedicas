from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def configure_database(app):
    """
    Configura la base de datos para la aplicación Flask utilizando SQLAlchemy.
    La URI de la base de datos se carga desde la variable de entorno 'DATABASE_URL'.
    """
    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        raise ValueError("DATABASE_URL no está configurado en las variables de entorno")

    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desactivar para mejorar el rendimiento
    db.init_app(app)
