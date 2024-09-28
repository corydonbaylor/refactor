from flask import Blueprint

python_package_bp = Blueprint('python_package', __name__, template_folder='templates')

from . import routes