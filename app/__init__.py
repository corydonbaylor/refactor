from flask import Flask
from .travel import travel_bp
from .coding import coding_bp
from .statistics import statistics_bp
from .tutorials import tutorials_bp
from .main import main_bp
from .tutorials.python_r import python_r_bp
from .tutorials.python_package import python_package_bp
from .tutorials.docker import docker_bp
from .tutorials.flask_pi import flask_pi_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(travel_bp, url_prefix='/travel')
    app.register_blueprint(coding_bp, url_prefix='/coding')
    app.register_blueprint(statistics_bp, url_prefix='/statistics')
    app.register_blueprint(tutorials_bp, url_prefix='/tutorials')
    app.register_blueprint(python_r_bp, url_prefix='/tutorials/python-r')
    app.register_blueprint(python_package_bp, url_prefix='/tutorials/python-package')
    app.register_blueprint(docker_bp, url_prefix='/tutorials/docker')
    app.register_blueprint(flask_pi_bp, url_prefix='/tutorials/flask-pi')

    app.register_blueprint(main_bp)  

    return app