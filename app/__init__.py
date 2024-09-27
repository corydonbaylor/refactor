from flask import Flask
from .travel import travel_bp
from .coding import coding_bp
from .statistics import statistics_bp
from .tutorials import tutorials_bp
from .main import main_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(travel_bp, url_prefix='/travel')
    app.register_blueprint(coding_bp, url_prefix='/coding')
    app.register_blueprint(statistics_bp, url_prefix='/statistics')
    app.register_blueprint(tutorials_bp, url_prefix='/tutorials')
    app.register_blueprint(main_bp)  

    return app