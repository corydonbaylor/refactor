from flask import Blueprint

claude_robot_bp = Blueprint('claude_robot', __name__, template_folder='templates', static_folder='resources')

from . import routes