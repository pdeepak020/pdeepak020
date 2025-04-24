import os
from flask import Flask, render_template, request, send_file, flash, redirect, url_for
from werkzeug.utils import secure_filename
import img2pdf
from PIL import Image
import docx2pdf
from pdf2docx import Converter
import tempfile

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for flashing messages

# Configure upload folder - use absolute path
UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'uploads'))
ALLOWED_EXTENSIONS = {
    'document': {'docx', 'pdf', 'txt'},
    'image': {'png', 'jpg', 'jpeg', 'gif', 'bmp'}
}

# Ensure upload directory exists with proper permissions
try:
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    # Test write permissions
    test_file = os.path.join(UPLOAD_FOLDER, 'test.txt')
    with open(test_file, 'w') as f:
        f.write('test')
    os.remove(test_file)
except Exception as e:
    print(f"Error setting up upload directory: {str(e)}")
    raise

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

def allowed_file(filename, file_type):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS[file_type]

def get_file_type(filename):
    ext = filename.rsplit('.', 1)[1].lower() if '.' in filename else ''
    if ext in ALLOWED_EXTENSIONS['image']:
        return 'image'
    return 'document'

def safe_remove_file(file_path):
    """Safely remove a file if it exists"""
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        print(f"Error removing file {file_path}: {str(e)}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_file():
    if 'file' not in request.files:
        flash('No file selected')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('No file selected')
        return redirect(request.url)

    if file:
        try:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            # Ensure the upload directory exists
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            
            file.save(file_path)
            print(f"File saved to: {file_path}")  # Debug log
            
            file_type = get_file_type(filename)
            target_format = request.form.get('target_format')
            
            if not target_format:
                flash('No target format selected')
                return redirect(url_for('index'))
            
            try:
                if file_type == 'image' and target_format == 'pdf':
                    # Convert image to PDF
                    output_path = os.path.join(app.config['UPLOAD_FOLDER'], 
                                             f"{os.path.splitext(filename)[0]}.pdf")
                    with open(file_path, "rb") as image_file:
                        pdf_bytes = img2pdf.convert(image_file)
                    
                    with open(output_path, "wb") as pdf_file:
                        pdf_file.write(pdf_bytes)
                    
                    return send_file(
                        output_path,
                        as_attachment=True,
                        download_name=f"{os.path.splitext(filename)[0]}.pdf"
                    )
                
                elif file_type == 'document':
                    if filename.endswith('.docx') and target_format == 'pdf':
                        # Convert DOCX to PDF
                        output_path = os.path.join(app.config['UPLOAD_FOLDER'], 
                                                 f"{os.path.splitext(filename)[0]}.pdf")
                        docx2pdf.convert(file_path, output_path)
                        return send_file(
                            output_path,
                            as_attachment=True,
                            download_name=f"{os.path.splitext(filename)[0]}.pdf"
                        )
                    
                    elif filename.endswith('.pdf') and target_format == 'docx':
                        # Convert PDF to DOCX using the Converter class
                        output_path = os.path.join(app.config['UPLOAD_FOLDER'], 
                                                 f"{os.path.splitext(filename)[0]}.docx")
                        # Create a Converter object and convert the PDF to DOCX
                        cv = Converter(file_path)
                        cv.convert(output_path)
                        cv.close()
                        return send_file(
                            output_path,
                            as_attachment=True,
                            download_name=f"{os.path.splitext(filename)[0]}.docx"
                        )
                
                flash('Unsupported conversion')
                return redirect(url_for('index'))
                
            except Exception as e:
                flash(f'Error during conversion: {str(e)}')
                return redirect(url_for('index'))
            finally:
                # Clean up temporary files
                safe_remove_file(file_path)
                if 'output_path' in locals():
                    safe_remove_file(output_path)
                    
        except Exception as e:
            flash(f'Error processing file: {str(e)}')
            return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True) 