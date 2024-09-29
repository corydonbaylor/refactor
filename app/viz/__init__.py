from flask import Blueprint

viz_bp = Blueprint('viz', __name__, template_folder='templates', static_folder='resources', static_url_path='/static')

from . import routes
