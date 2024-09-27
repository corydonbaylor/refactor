from flask import render_template
from . import statistics_bp

@statistics_bp.route('/')
def statistics():
    return render_template('statistics.html')