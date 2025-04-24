# Advanced Image Processing Web Application

A web application for processing images using Python, Flask, OpenCV, NumPy, and Matplotlib.

## Features

- Upload images (JPG, PNG, GIF)
- Apply various image processing operations:
  - Grayscale conversion
  - Blur effect
  - Sharpen effect
  - Rotation
  - Flip (horizontal/vertical)
  - Brightness adjustment
  - Contrast adjustment
  - Resize
  - Edge detection (Canny)
  - Color shift
  - Histogram visualization
  - Thresholding
- Preview images before processing
- Download processed images

## Technologies Used

- **Flask**: Web framework
- **OpenCV (cv2)**: Advanced image processing
- **NumPy**: Numerical operations on image data
- **Matplotlib**: Data visualization and histogram generation
- **Pillow (PIL)**: Basic image processing (legacy support)
- **Werkzeug**: Utilities for WSGI applications
- **python-dotenv**: Environment variable management

## Installation

1. Clone this repository or download the source code.

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the application:
   ```
   python run.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

3. Upload an image and select the desired processing operation.

4. Adjust the operation parameters if needed.

5. Click "Process Image" to apply the selected operation.

6. View the result and download the processed image if desired.

## Project Structure

```
imageprocessor/
├── app/
│   ├── __init__.py      # Flask application initialization
│   ├── routes.py         # Route definitions
│   ├── static/
│   │   ├── uploads/      # Directory for uploaded images
│   │   └── processed/    # Directory for processed images
│   └── templates/
│       ├── index.html    # Main page with upload form
│       └── result.html   # Results page
├── requirements.txt      # Project dependencies
├── README.md            # This file
└── run.py               # Application entry point
```

## Advanced Features

### Edge Detection
Uses OpenCV's Canny edge detection algorithm to identify edges in the image. Adjust the threshold values to control the sensitivity of edge detection.

### Color Shift
Modifies the color channels of the image. Currently supports shifting the red channel to create color effects.

### Histogram Visualization
Generates a color histogram using Matplotlib, showing the distribution of pixel values across the RGB channels.

### Thresholding
Converts the image to binary (black and white) based on a threshold value. Useful for segmentation and object detection.

## License

This project is open source and available under the MIT License. 