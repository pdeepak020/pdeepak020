from flask import Flask
from flask import render_template, request, redirect, url_for, flash, send_from_directory
import os
from werkzeug.utils import secure_filename
from PIL import Image, ImageEnhance, ImageFilter
import uuid
import cv2
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
app.config['PROCESSED_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'processed')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload size
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Ensure upload and processed directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def process_image(image_path, operation, params=None):
    """
    Process the image based on the selected operation using OpenCV, NumPy, and Matplotlib
    """
    # Read image with OpenCV
    img = cv2.imread(image_path)
    
    # Convert BGR to RGB for display
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    if operation == 'grayscale':
        # Convert to grayscale using OpenCV
        processed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Convert back to RGB for saving
        processed_img_rgb = cv2.cvtColor(processed_img, cv2.COLOR_GRAY2RGB)
    
    elif operation == 'blur':
        # Apply Gaussian blur
        radius = params.get('radius', 2) if params else 2
        kernel_size = int(radius * 2 + 1)  # Ensure odd kernel size
        processed_img = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)
        processed_img_rgb = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
    
    elif operation == 'sharpen':
        # Apply sharpening filter
        kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        processed_img = cv2.filter2D(img, -1, kernel)
        processed_img_rgb = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
    
    elif operation == 'rotate':
        # Rotate image
        angle = params.get('angle', 90) if params else 90
        height, width = img.shape[:2]
        center = (width // 2, height // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        processed_img = cv2.warpAffine(img, rotation_matrix, (width, height), flags=cv2.INTER_LINEAR)
        processed_img_rgb = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
    
    elif operation == 'flip':
        # Flip image
        direction = params.get('direction', 'horizontal') if params else 'horizontal'
        if direction == 'horizontal':
            processed_img = cv2.flip(img, 1)  # 1 for horizontal flip
        else:
            processed_img = cv2.flip(img, 0)  # 0 for vertical flip
        processed_img_rgb = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
    
    elif operation == 'brightness':
        # Adjust brightness
        factor = params.get('factor', 1.5) if params else 1.5
        processed_img = cv2.convertScaleAbs(img, alpha=factor, beta=0)
        processed_img_rgb = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
    
    elif operation == 'contrast':
        # Adjust contrast
        factor = params.get('factor', 1.5) if params else 1.5
        processed_img = cv2.convertScaleAbs(img, alpha=factor, beta=128*(1-factor))
        processed_img_rgb = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
    
    elif operation == 'resize':
        # Resize image
        width = params.get('width', 800) if params else 800
        height = params.get('height', 600) if params else 600
        processed_img = cv2.resize(img, (width, height), interpolation=cv2.INTER_LANCZOS4)
        processed_img_rgb = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
    
    elif operation == 'edge_detection':
        # Edge detection using Canny
        threshold1 = params.get('threshold1', 100) if params else 100
        threshold2 = params.get('threshold2', 200) if params else 200
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        processed_img = cv2.Canny(gray, threshold1, threshold2)
        # Convert to RGB for saving
        processed_img_rgb = cv2.cvtColor(processed_img, cv2.COLOR_GRAY2RGB)
    
    elif operation == 'color_shift':
        # Shift colors (e.g., increase red channel)
        shift = params.get('shift', 50) if params else 50
        b, g, r = cv2.split(img)
        r = cv2.add(r, shift)
        processed_img = cv2.merge([b, g, r])
        processed_img_rgb = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
    
    elif operation == 'histogram':
        # Generate histogram visualization
        plt.figure(figsize=(10, 6))
        color = ('b', 'g', 'r')
        for i, col in enumerate(color):
            histr = cv2.calcHist([img], [i], None, [256], [0, 256])
            plt.plot(histr, color=col)
        plt.title('Color Histogram')
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')
        
        # Save the histogram to a bytes buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()
        
        # Convert to base64 for embedding in HTML
        histogram_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
        
        # For the processed image, we'll use the original image
        processed_img_rgb = img_rgb
        
        # Generate a unique filename for the processed image
        filename = secure_filename(os.path.basename(image_path))
        unique_filename = f"{uuid.uuid4()}_{filename}"
        output_path = os.path.join(app.config['PROCESSED_FOLDER'], unique_filename)
        
        # Save the original image
        cv2.imwrite(output_path, img)
        
        return unique_filename, histogram_base64
    
    elif operation == 'threshold':
        # Apply thresholding
        threshold = params.get('threshold', 127) if params else 127
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, processed_img = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
        processed_img_rgb = cv2.cvtColor(processed_img, cv2.COLOR_GRAY2RGB)
    
    else:
        # Default: return original image
        processed_img_rgb = img_rgb
    
    # Generate a unique filename for the processed image
    filename = secure_filename(os.path.basename(image_path))
    unique_filename = f"{uuid.uuid4()}_{filename}"
    output_path = os.path.join(app.config['PROCESSED_FOLDER'], unique_filename)
    
    # Save the processed image using OpenCV
    cv2.imwrite(output_path, cv2.cvtColor(processed_img_rgb, cv2.COLOR_RGB2BGR))
    
    return unique_filename

from app import routes 