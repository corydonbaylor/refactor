from flask import Blueprint

# Create a Blueprint for the main section of the application
main_bp = Blueprint('main', __name__, template_folder='templates', static_folder='resources')

# Import routes to register them with this blueprint
from . import routes