from flask import render_template, request
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


# Dictionary of available CSV files
CSV_FILES = {
    'NYC': 'app/viz/resources/maps/nyc.csv',
    'Boston': 'app/viz/resources/maps/boston.csv',
    'Chicago': 'app/viz/resources/maps/chicago.csv'
}

@viz_bp.route('/map', methods=['GET', 'POST'])
def map_view():
    selected_file = None  # Default value for selected file
    map_html = None       # Default value for the map HTML
    if request.method == 'POST':
        # Get the selected file from the form
        selected_file = request.form.get('csv_file')

        # Get the file path based on the selection
        file_path = CSV_FILES.get(selected_file)
        print(file_path)
        if not file_path or not os.path.exists(file_path):
            return f"Error: The selected file '{selected_file}' does not exist.", 404

        # Load coordinates from the selected CSV file
        data = pd.read_csv(file_path)

        # Create a Folium map centered at the average coordinates
        center = [data['lat'].mean(), data['long'].mean()]
        m = folium.Map(location=center, zoom_start=12, tiles="cartodb positron")

        # Add circles for each coordinate in the CSV
        for _, row in data.iterrows():
            folium.Circle(
                location=(row['lat'], row['long']),
                radius=600,  # Set the desired radius in meters
                color='#2a66ad',
                fill=True,
                fill_color='#2a66ad',
                fill_opacity=0.5,
            ).add_to(m)

        # Render the map as HTML
        map_html = m._repr_html_()

    return render_template('maps.html', csv_files=CSV_FILES.keys(), selected_file=selected_file, map_html=map_html)
