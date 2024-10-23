from flask import Blueprint

examples_bp = Blueprint('examples', __name__, template_folder='templates', static_folder='resources', static_url_path='/static')

from . import routes