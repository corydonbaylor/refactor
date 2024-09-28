from flask import render_template
from . import flask_pi_bp

@flask_pi_bp.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap.html')

@flask_pi_bp.route('/flask')
def flask():
    return render_template('flask.html')

@flask_pi_bp.route('/html_css')
def html_css():
    return render_template('html_css.html')

@flask_pi_bp.route('/linux_git')
def linux_git():
    return render_template('linux_git.html')

@flask_pi_bp.route('/apache')
def apache():
    return render_template('apache.html')

@flask_pi_bp.route('/port_forwarding')
def port_forwarding():
    return render_template('port_forwarding.html')

@flask_pi_bp.route('/templates')
def templates():
    return render_template('templates.html')

@flask_pi_bp.route('/using_raspberry')
def using_raspberry():
    return render_template('using_raspberry.html')