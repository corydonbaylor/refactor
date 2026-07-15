from flask import render_template
from . import claude_robot_bp

@claude_robot_bp.route('/assemble')
def assemble():
    return render_template('assemble.html')

@claude_robot_bp.route('/code')
def code():
    return render_template('code.html')

@claude_robot_bp.route('/brain')
def brain():
    return render_template('brain.html')

@claude_robot_bp.route('/eyes')
def eyes():
    return render_template('eyes.html')