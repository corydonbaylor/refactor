from flask import request, make_response, render_template, redirect, url_for
from . import utils_bp  # Correctly importing the blueprint
from .password import password_required  # Import the decorator directly

@utils_bp.route('/error', methods=['GET', 'POST'])
def error():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == "friends":  # Replace with your actual password
            resp = make_response(redirect(url_for('main.index')))  # Adjust if needed
            resp.set_cookie('password', password)
            return resp
        else:
            return "Invalid Password", 403

    return render_template('error.html', bg_class='index')  # Ensure this template exists


