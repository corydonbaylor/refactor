from flask import render_template
from . import python_package_bp

@python_package_bp.route('/class')
def class1():
    return render_template('class.html')

@python_package_bp.route('/class2')
def class2():
    return render_template('class2.html')

@python_package_bp.route('/functions')
def functions():
    return render_template('functions.html')

@python_package_bp.route('/functions2')
def functions2():
    return render_template('functions2.html')

@python_package_bp.route('/package')
def package():
    return render_template('package.html')

@python_package_bp.route('/poetry')
def poetry():
    return render_template('poetry.html')

@python_package_bp.route('/pytest')
def pytest():
    return render_template('pytest.html')