import cv2
import numpy as np

def make_sketch(image_array):
    gray = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
    inv = cv2.bitwise_not(gray)
    blur = cv2.GaussianBlur(inv, (21, 21), sigmaX=0, sigmaY=0)
    sketch = cv2.divide(gray, 255 - blur, scale=128)
    return sketch
