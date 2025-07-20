# Pencil Sketch App

This file is ready for GitHub and matches the instructions/code from the original version (Streamlit + OpenCV, simple pencil effect).

# Image to Pencil Sketch Web App

A simple and quick web app that converts images to pencil sketches using Streamlit, OpenCV, and Python.

## Features

- Upload and preview JPG/JPEG/PNG images
- Instantly view a pencil sketch of your image
- Download your sketch result


## Requirements

- Python 3.7 or newer
- Packages as listed below


## Project Structure

```
pencil-sketch-app/
│
├── app.py
├── requirements.txt
└── (optional) samples/
```


## Setup \& Installation

1. **Create and activate a virtual environment** (recommended):

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

2. **Add and install dependencies**
Create `requirements.txt` in your project folder:

```
streamlit
opencv-python
numpy
pillow
```

Then install:

```bash
pip install -r requirements.txt
```


## Usage

1. **Run the app:**

```bash
streamlit run app.py
```

2. **Open** the browser link displayed (usually `http://localhost:8501/`).
3. **Upload** any image, view both the original and sketch, and download your result.


## How It Works

- **Grayscale**: Converts uploaded photo to black and white.
- **Invert \& Blur**: Inverts and blurs to create a highlight mask.
- **Dodge Blend**: Blends the grayscale and blurred images in a way that mimics pencil strokes.


## License

This project is provided under the MIT License.

Have fun turning your photos into sketches!

