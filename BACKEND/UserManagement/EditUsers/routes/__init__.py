from .user import user_blueprint

def init_routes(app):
    # Register the user blueprint
    app.register_blueprint(user_blueprint)
