import cv2
import os

current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, '..', 'data', 'Test Image.png')

image = cv2.imread(image_path)
if image is None:
    print(f"Error: Unable to load image from {image_path}")
    exit(1)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresholded_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('Thresholded Image', thresholded_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
