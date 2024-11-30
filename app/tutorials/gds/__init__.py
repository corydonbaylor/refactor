from flask import Blueprint

gds_bp = Blueprint('gds', __name__, template_folder='templates', static_folder='resources')

from . import routes