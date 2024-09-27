from flask import render_template
from . import coding_bp

@coding_bp.route('/')
def coding():
    return render_template('coding.html')
