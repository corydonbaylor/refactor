from flask import Blueprint

nyc_subway_bp = Blueprint('nyc_subway', __name__, template_folder='templates')

from . import routes