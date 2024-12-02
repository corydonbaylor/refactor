from flask import render_template
from . import gds_bp

@gds_bp.route('/dijkstra')
def dijkstra():
    return render_template('shortest.html')

@gds_bp.route('/centrality')
def centrality():
    return render_template('centrality.html')

@gds_bp.route('/pagerank')
def pagerank():
    return render_template('pagerank.html')

@gds_bp.route('/modularity')
def modularity():
    return render_template('modularity.html')