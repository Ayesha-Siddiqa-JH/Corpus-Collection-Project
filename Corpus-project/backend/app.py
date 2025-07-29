from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from routes.text import text_bp
from routes.audio import audio_bp
from routes.image import image_bp
from database import init_db

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Initialize database
init_db()

# Register blueprints
app.register_blueprint(text_bp, url_prefix='/text')
app.register_blueprint(audio_bp, url_prefix='/audio')
app.register_blueprint(image_bp, url_prefix='/image')

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
