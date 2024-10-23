from flask import Flask, request, render_template
from neo4j import GraphDatabase
from fuzzywuzzy import process
from dotenv import load_dotenv
import os
from . import nyc_subway_bp

load_dotenv()

URI = os.getenv('NEO4J_URI')
USER = os.getenv('NEO4J_USER')
PASSWORD = os.getenv('NEO4J_PASSWORD')

# Create Neo4j driver
driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))

def load_stations_from_file(filename='stations.txt'):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, filename)
    with open(file_path, 'r') as f:
        return [line.strip() for line in f]

all_stations = load_stations_from_file()

def get_shortest_path(tx, start_station, end_station):
    query = """
    MATCH (start:Station {name: $start_name}), (end:Station {name: $end_name})
    CALL gds.shortestPath.dijkstra.stream('subway_graph', {
      sourceNode: id(start),
      targetNode: id(end),
      relationshipWeightProperty: 'length'
    })
    YIELD path
    RETURN [node in nodes(path) | {
      name: node.name,
      latitude: node.latitude,
      longitude: node.longitude
    }] AS stations
    """
    result = tx.run(query, start_name=start_station, end_name=end_station)
    return result.single()

def get_station_suggestions(input_name, limit=5):
    return process.extract(input_name, all_stations, limit=limit)

@nyc_subway_bp.route('/')
def index():
    return render_template('map_index.html')

@nyc_subway_bp.route('/shortest_path', methods=['GET'])
def shortest_path():
    start = request.args.get('start')
    end = request.args.get('end')
    
    if not start or not end:
        return render_template('map_index.html', error="Please provide both start and end stations")

    if start not in all_stations:
        start_suggestions = get_station_suggestions(start)
        return render_template('map_index.html', error=f"Start station '{start}' not found", start_suggestions=start_suggestions)
    
    if end not in all_stations:
        end_suggestions = get_station_suggestions(end)
        return render_template('map_index.html', error=f"End station '{end}' not found", end_suggestions=end_suggestions)
    
    with driver.session() as session:
        result = session.read_transaction(get_shortest_path, start, end)
    
    if result:
        return render_template('map.html', 
                               start_station=start, 
                               end_station=end, 
                               stations=result["stations"])
    else:
        return render_template('map_index.html', error="No path found between the specified stations")
