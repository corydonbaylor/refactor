from flask import render_template
from . import examples_bp

@examples_bp.route('/')
def examples():
    return "<h1>Welcome to the Examples Page</h1>"