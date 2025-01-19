from flask import render_template
from . import viz_bp
import folium
import pandas as pd
import os

@viz_bp.route('/')
def statistics():
    return render_template('viz.html', bg_class='index')

@viz_bp.route('/barchart_race')
def barchart():
    return render_template('barchart_race.html')

@viz_bp.route('/calendar')
def calendar():
    return render_template('calendar.html')

@viz_bp.route('/covid')
def covid():
    return render_template('covid.html')

@viz_bp.route('/grammys')
def grammys():
    return render_template('grammys.html')

@viz_bp.route('/joyplot')
def joyplot():
    return render_template('joyplot.html')

@viz_bp.route('/powerfive')
def powerfive():
    return render_template('powerfive.html')

@viz_bp.route('/rock')
def rock():
    return render_template('rock.html')

@viz_bp.route('/map')
def map_view():
    # Load coordinates from CSV
    data = pd.read_csv('app/viz/resources/maps/nyc.csv')

    # Create a Folium map centered at the average coordinates
    center = [data['lat'].mean(), data['long'].mean()]
    m = folium.Map(location=center, zoom_start=14)

    # Add circles for each coordinate in the CSV
    for _, row in data.iterrows():
        folium.Circle(
            location=(row['lat'], row['long']),
            radius=804,  # Set the desired radius in meters
            color='blue',
            fill=True,
            fill_color='blue',
            fill_opacity=0.3,
        ).add_to(m)

    # Render the map as HTML
    map_html = m._repr_html_()

    return render_template('maps.html', map_html=map_html)