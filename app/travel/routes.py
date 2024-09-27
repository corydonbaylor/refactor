from flask import render_template
from . import travel_bp

@travel_bp.route('/')
def travel():
    return render_template('travel.html')