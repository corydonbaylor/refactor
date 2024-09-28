from flask import Blueprint

flask_pi_bp = Blueprint('flask_pi', __name__, template_folder='templates')

from . import routes