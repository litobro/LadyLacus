from flask import Flask, render_template, request, send_file, redirect
import pylacus
import io
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyLacus instance (adjust root_url as needed)
lacus_url = os.environ.get('LACUS_URL', 'http://localhost:7100')
lacus = pylacus.PyLacus(lacus_url)
CaptureStatus = pylacus.CaptureStatus

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    capture_id = None
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            # Enqueue screenshot job using PyLacus instance
            capture_id = lacus.enqueue(url=url)
            # Redirect to permalink result page
            return redirect(f'/result/{capture_id}')
    return render_template('index.html', capture_id=None)

@app.route('/result/<capture_id>')
def result(capture_id):
    return render_template('result.html', capture_id=capture_id)

@app.route('/status/<capture_id>')
def status(capture_id):
    capture_status = lacus.get_capture_status(capture_id)
    # Status 1 means ready (see PyLacus docs)
    if capture_status == CaptureStatus.DONE:
        return {'ready': True, 'image_url': f'/screenshot/{capture_id}'}
    else:
        return {'ready': False, 'status': CaptureStatus(capture_status).name}

@app.route('/screenshot/<capture_id>')
def screenshot(capture_id):
    capture_status = lacus.get_capture_status(capture_id)
    if capture_status != 1:
        return "Screenshot not ready", 202
    # Use decode=True to get bytes, as per PyLacus API
    capture = lacus.get_capture(capture_id, decode=True)
    # Try both attribute and dict access for compatibility
    png_bytes = None
    if hasattr(capture, 'png') and capture.png:
        png_bytes = capture.png
    elif isinstance(capture, dict) and 'png' in capture and capture['png']:
        png_bytes = capture['png']
    if not png_bytes:
        return "No screenshot available", 404
    return send_file(
        io.BytesIO(png_bytes),
        mimetype='image/png',
        as_attachment=False,
        download_name=f'screenshot_{capture_id}.png'
    )

if __name__ == '__main__':
    app.run(debug=True)
