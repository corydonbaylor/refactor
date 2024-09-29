from flask import Blueprint

travel_bp = Blueprint('travel', __name__, template_folder='templates', static_folder='resources')

from . import routes