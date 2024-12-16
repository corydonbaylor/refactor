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

@gds_bp.route('/louvain')
def louvain():
    return render_template('louvain.html')

@gds_bp.route('/link_prediction')
def link_prediction():
    return render_template('link_prediction.html')


@gds_bp.route('/top_sort')
def top_sort():
    return render_template('top_sort.html')