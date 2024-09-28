from flask import render_template
from . import docker_bp

@docker_bp.route('/hello_docker')
def hello_docker():
    return render_template('hello_docker.html')

@docker_bp.route('/manage_docker')
def manage_docker():
    return render_template('manage_docker.html')

@docker_bp.route('/write_docker')
def write_docker():
    return render_template('write_docker.html')