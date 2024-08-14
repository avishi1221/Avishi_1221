import cv2
import numpy as np

# Load image
image_path = r"C:\Users\Admin\Desktop\other try cones v5\Data Augmentaded - Cone dataset.v1i.yolov5pytorch\train\images\4_z8126b7d060d92d74599e0618_f101c6b90f14b1643_d20161224_m042323_c001_v0001032_t0029_png.rf.1e1183561b5ca5684882f14e3dde7dfa.jpg"
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply binary thresholding
_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Define structuring element (kernel)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

# Apply morphological operations

# Dilation
dilated_image = cv2.dilate(binary_image, kernel, iterations=1)

# Erosion
eroded_image = cv2.erode(binary_image, kernel, iterations=1)

# Opening
opened_image = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)

# Closing
closed_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

# Morphological Gradient
gradient_image = cv2.morphologyEx(binary_image, cv2.MORPH_GRADIENT, kernel)

# Top Hat (White Hat)
top_hat_image = cv2.morphologyEx(binary_image, cv2.MORPH_TOPHAT, kernel)

# Black Hat
black_hat_image = cv2.morphologyEx(binary_image, cv2.MORPH_BLACKHAT, kernel)

# Display images
cv2.imshow('Original Image', image)
cv2.imshow('Gray Image', gray_image)
cv2.imshow('Binary Image', binary_image)
cv2.imshow('Dilated Image', dilated_image)
cv2.imshow('Eroded Image', eroded_image)
cv2.imshow('Opened Image', opened_image)
cv2.imshow('Closed Image', closed_image)
cv2.imshow('Gradient Image', gradient_image)
cv2.imshow('Top Hat Image', top_hat_image)
cv2.imshow('Black Hat Image', black_hat_image)

# Wait and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
