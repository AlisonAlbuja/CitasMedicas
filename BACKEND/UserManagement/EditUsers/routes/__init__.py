from .user import user_blueprint

def init_routes(app):
    # Registrar el blueprint de usuarios
    app.register_blueprint(user_blueprint)
