from flask import render_template
from . import viz_bp

@viz_bp.route('/')
def statistics():
    return render_template('viz.html', bg_class='index')

@viz_bp.route('/barchart_race')
def barchart():
    return render_template('barchart_race.html')

@viz_bp.route('/calendar')
def calendar():
    return render_template('calendar.html')

@viz_bp.route('/covid')
def covid():
    return render_template('covid.html')

@viz_bp.route('/grammys')
def grammys():
    return render_template('grammys.html')

@viz_bp.route('/joyplot')
def joyplot():
    return render_template('joyplot.html')

@viz_bp.route('/powerfive')
def powerfive():
    return render_template('powerfive.html')

@viz_bp.route('/rock')
def rock():
    return render_template('rock.html')