from flask import render_template
from . import main_bp

@main_bp.route('/')
def index():
    print("Index route accessed")  # Debugging output to confirm route access
    # template_path = os.path.join(app.root_path, 'main', 'templates', 'index.html')
    # print(f"Looking for template at: {template_path}")  
    return render_template('index.html')