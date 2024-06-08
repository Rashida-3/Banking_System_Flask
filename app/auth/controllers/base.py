from flask import render_template
from app.auth import index_bp

@index_bp.route('/')
def index():
    return render_template('index.html')

