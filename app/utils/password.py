from flask import request, redirect, make_response, url_for, abort
from functools import wraps

# Define the password (you might want to store this securely)
PASSWORD = "friends"

def password_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check for the password in cookies
        password_cookie = request.cookies.get('password')

        if password_cookie != PASSWORD:
            # If the password is incorrect or not set, redirect to a login page or show an error
            return redirect(url_for('utils.error'))

        return f(*args, **kwargs)

    return decorated_function

def login():
    # This function will handle the login logic
    # You can render a simple login form or handle password submission here.
    pass