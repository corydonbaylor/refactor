from flask import render_template
from . import travel_bp
from ..utils import password_required

@travel_bp.route('/')
def travel():
    return render_template('travel.html', bg_class="heroes")

@travel_bp.route('/argentina')
def argentina():
    return render_template('argentina.html')

@travel_bp.route('/costa_rica')
def costa_rica():
    return render_template('costa_rica.html')

@travel_bp.route('/france')
@password_required
def france():
    return render_template('france.html')

@travel_bp.route('/hungary')
@password_required
def hungary():
    return render_template('hungary.html')

@travel_bp.route('/iceland')
def iceland():
    return render_template('iceland.html')

@travel_bp.route('/ireland')
def ireland():
    return render_template('ireland.html')

@travel_bp.route('/med')
@password_required
def med():
    return render_template('med.html')

@travel_bp.route('/mexico')
@password_required
def mexico():
    return render_template('mexico.html')

@travel_bp.route('/puerto_rico')
@password_required
def puerto_rico():
    return render_template('puerto_rico.html')

@travel_bp.route('/quebec')
def quebec():
    return render_template('quebec.html')

@travel_bp.route('/italy')
@password_required
def italy():
    return render_template('italy.html')

@travel_bp.route('/southwest')
def southwest():
    return render_template('southwest.html')

@travel_bp.route('/uruguay')
@password_required
def uruguay():
    return render_template('uruguay.html')