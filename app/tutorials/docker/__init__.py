from flask import Blueprint

docker_bp = Blueprint('docker', __name__, template_folder='templates')

from . import routes