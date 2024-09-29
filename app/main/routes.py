from flask import render_template
from . import main_bp

@main_bp.route('/')
def index():
    print("Index route accessed")  # Debugging output to confirm route access
    return render_template('index.html', bg_class='index')