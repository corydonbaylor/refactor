from flask import Blueprint

coding_bp = Blueprint('coding', __name__, template_folder='templates')

from . import routes