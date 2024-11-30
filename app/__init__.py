from flask import Flask
from .travel import travel_bp
from .coding import coding_bp
from .viz import viz_bp
from .tutorials import tutorials_bp
from .main import main_bp
from .tutorials.python_r import python_r_bp
from .tutorials.python_package import python_package_bp
from .tutorials.docker import docker_bp
from .tutorials.flask_pi import flask_pi_bp
from .tutorials.machine_learning import machine_learning_bp
from .tutorials.gds import gds_bp
from .examples.nyc_subway import nyc_subway_bp
from .utils import utils_bp

from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.register_blueprint(travel_bp, url_prefix='/travel')
    app.register_blueprint(coding_bp, url_prefix='/coding')
    app.register_blueprint(viz_bp, url_prefix='/viz')
    app.register_blueprint(tutorials_bp, url_prefix='/tutorials')
    
    app.register_blueprint(python_r_bp, url_prefix='/tutorials/python-r')
    app.register_blueprint(python_package_bp, url_prefix='/tutorials/python-package')
    app.register_blueprint(docker_bp, url_prefix='/tutorials/docker')
    app.register_blueprint(flask_pi_bp, url_prefix='/tutorials/flask-pi')
    app.register_blueprint(machine_learning_bp, url_prefix='/tutorials/machine_learning')
    app.register_blueprint(gds_bp, url_prefix='/tutorials/gds')


    app.register_blueprint(nyc_subway_bp, url_prefix='/examples/nyc')

    app.register_blueprint(main_bp)  
    app.register_blueprint(utils_bp)
    return app