from .operadoras import operadoras_bp

def register_routes(app):
    app.register_blueprint(operadoras_bp, url_prefix='/api')
