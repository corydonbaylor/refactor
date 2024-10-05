from flask import Blueprint

machine_learning_bp = Blueprint('machine_learning', __name__, template_folder='templates', static_folder='resources')

from . import routes