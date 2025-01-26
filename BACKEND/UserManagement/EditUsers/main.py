from flask import Flask
from database import configure_database
from routes import init_routes

def create_app():
    app = Flask(__name__)
    
    # Configurar la base de datos
    configure_database(app)
    
    # Registrar las rutas
    init_routes(app)
    
    # Ruta raíz
    @app.route("/")
    def home():
        return "¡Bienvenido al servicio de gestión de usuarios!"

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
