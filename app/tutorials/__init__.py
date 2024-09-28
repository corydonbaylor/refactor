from flask import Blueprint

tutorials_bp = Blueprint('tutorials', __name__, template_folder='templates', static_folder='resources')

from . import routes