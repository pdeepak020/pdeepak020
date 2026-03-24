from app import app, allowed_file, process_image
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
import os

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    
    # If user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Get the selected operation and parameters
        operation = request.form.get('operation', 'grayscale')
        params = {}
        
        # Get operation-specific parameters
        if operation == 'blur':
            params['radius'] = float(request.form.get('radius', 2))
        elif operation == 'rotate':
            params['angle'] = int(request.form.get('angle', 90))
        elif operation == 'flip':
            params['direction'] = request.form.get('direction', 'horizontal')
        elif operation == 'brightness':
            params['factor'] = float(request.form.get('brightness_factor', 1.5))
        elif operation == 'contrast':
            params['factor'] = float(request.form.get('contrast_factor', 1.5))
        elif operation == 'resize':
            params['width'] = int(request.form.get('width', 800))
            params['height'] = int(request.form.get('height', 600))
        elif operation == 'edge_detection':
            params['threshold1'] = int(request.form.get('threshold1', 100))
            params['threshold2'] = int(request.form.get('threshold2', 200))
        elif operation == 'color_shift':
            params['shift'] = int(request.form.get('shift', 50))
        elif operation == 'threshold':
            params['threshold'] = int(request.form.get('threshold', 127))
        
        # Process the image
        result = process_image(file_path, operation, params)
        
        # Check if the result is a tuple (for histogram operation)
        if isinstance(result, tuple):
            processed_filename, histogram_base64 = result
            # Return the processed image with histogram
            return render_template('result.html', 
                                original_filename=filename, 
                                processed_filename=processed_filename,
                                operation=operation,
                                histogram_base64=histogram_base64)
        else:
            processed_filename = result
            # Return the processed image
            return render_template('result.html', 
                                original_filename=filename, 
                                processed_filename=processed_filename,
                                operation=operation)
    
    flash('File type not allowed')
    return redirect(request.url)

@app.route('/static/processed/<filename>')
def processed_file(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER'], filename)

@app.route('/static/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename) 