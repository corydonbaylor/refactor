from flask import render_template
from . import docker_bp

@docker_bp.route('/hello_docker')
def hello_docker():
    return render_template('hello_docker.html')

@docker_bp.route('/manage_docker')
def manage_docker():
    return render_template('manage_docker.html')

@docker_bp.route('/flask_docker')
def flask_docker():
    return render_template('flask_docker.html')

@docker_bp.route('/poetry_docker')
def poetry_docker():
    return render_template('poetry_docker.html')

@docker_bp.route('/docker_hub')
def docker_hub():
    return render_template('docker_hub.html')