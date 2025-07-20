import streamlit as st
from PIL import Image
import numpy as np
import cv2

def make_sketch(image_array):
    gray = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
    inv = cv2.bitwise_not(gray)
    blur = cv2.GaussianBlur(inv, (21, 21), sigmaX=0, sigmaY=0)
    sketch = cv2.divide(gray, 255 - blur, scale=256)
    return sketch

st.title("Image to Pencil Sketch App 🎨✏️")
st.write("Upload an image and instantly see its pencil sketch.")

uploaded_file = st.file_uploader("Choose an Image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    input_image = Image.open(uploaded_file).convert("RGB")
    img_array = np.array(input_image)
    img_cv = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    sketch = make_sketch(img_cv)
    sketch_pil = Image.fromarray(sketch)

    # Show side by side using columns
    col1, col2 = st.columns(2)
    with col1:
        st.image(input_image, caption='Original Image', use_container_width=True)
    with col2:
        st.image(sketch_pil, caption='Pencil Sketch', use_container_width=True)

    st.download_button(
        label="Download Pencil Sketch",
        data=sketch_pil.tobytes(),
        file_name="pencil_sketch.png",
        mime="image/png"
    )
else:
    st.info("Please upload an image to begin.")
