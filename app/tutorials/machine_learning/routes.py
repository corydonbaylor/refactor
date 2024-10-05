from flask import render_template
from . import machine_learning_bp

@machine_learning_bp.route('/p_values')
def p_values():
    return render_template('p-values.html')

@machine_learning_bp.route('/linear_regeression')
def linear():
    return render_template('linear.html')

@machine_learning_bp.route('/kmeans')
def kmeans():
    return render_template('kmeans.html')

@machine_learning_bp.route('/classification_tree')
def class_tree():
    return render_template('class_tree.html')
