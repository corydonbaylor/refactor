from flask import render_template
from . import gds_bp

@gds_bp.route('/dijkstra')
def dijkstra():
    return render_template('shortest.html')