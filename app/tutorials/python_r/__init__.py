from flask import Blueprint

python_r_bp = Blueprint('python_r', __name__, template_folder='templates')

from . import routes