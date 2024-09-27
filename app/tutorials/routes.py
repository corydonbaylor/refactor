from flask import render_template
from . import tutorials_bp

@tutorials_bp.route('/')
def tutorials():
    return render_template('tutorials.html')