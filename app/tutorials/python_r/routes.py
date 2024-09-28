from flask import render_template
from . import python_r_bp

@python_r_bp.route('/combining')
def combining():
    return render_template('combining.html')

@python_r_bp.route('/data_types')
def data_types():
    return render_template('data_types.html')

@python_r_bp.route('/filtering')
def filtering():
    return render_template('filtering.html')

@python_r_bp.route('/groupby')
def groupby():
    return render_template('groupby.html')

@python_r_bp.route('/pandas')
def pandas():
    return render_template('pandas.html')

@python_r_bp.route('/reticulate')
def reticulate():
    return render_template('reticulate.html')

@python_r_bp.route('/save')
def save():
    return render_template('save.html')