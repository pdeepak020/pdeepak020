# File Converter Web Application

A modern web application that allows users to convert files between different formats and convert images to PDF.

## Features

- Convert DOCX files to PDF
- Convert PDF files to DOCX
- Convert images (PNG, JPG, JPEG, GIF, BMP) to PDF
- Drag and drop file upload
- Modern and responsive user interface
- File type validation
- Automatic file cleanup

## Requirements

- Python 3.8 or higher
- Flask
- Pillow
- python-docx
- pdf2docx
- docx2pdf
- img2pdf
- python-magic
- Werkzeug

## Installation

1. Clone the repository or download the files
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the application:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to `http://localhost:5000`
3. Upload a file by either:
   - Dragging and dropping it into the drop zone
   - Clicking the "Choose File" button
4. Select the target format from the dropdown menu
5. Click "Convert" to process the file
6. The converted file will be automatically downloaded

## Supported Conversions

- DOCX → PDF
- PDF → DOCX
- Images (PNG, JPG, JPEG, GIF, BMP) → PDF

## Notes

- Maximum file size: 16MB
- Temporary files are automatically cleaned up after conversion
- The application runs in debug mode by default

## License

This project is open source and available under the MIT License. 