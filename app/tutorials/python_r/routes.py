from flask import render_template
from . import python_r_bp

@python_r_bp.route('/')
def index():
    return render_template('python.html')