from flask import Blueprint

# Create the blueprint
utils_bp = Blueprint('utils', __name__, template_folder='templates')

# Import the password logic
from .password import password_required

# Import routes to register them with the blueprint
from . import routes  # Keep this at the end to avoid circular imports