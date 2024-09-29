from flask import render_template
from . import viz_bp

@viz_bp.route('/')
def statistics():
    return render_template('viz.html', bg_class='index')