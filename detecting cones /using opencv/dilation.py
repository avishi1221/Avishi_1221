import cv2
import numpy as np

# Load the binary image (convert to grayscale and apply a simple threshold to binarize)
image_path = r"C:\Users\Admin\Desktop\other try cones v5\Data Augmentaded - Cone dataset.v1i.yolov5pytorch\train\images\4_z8126b7d060d92d74599e0618_f101c6b90f14b1643_d20161224_m042323_c001_v0001032_t0029_png.rf.1e1183561b5ca5684882f14e3dde7dfa.jpg"
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply binary thresholding to convert grayscale image to binary
threshold_value = 127
_, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

# Define a kernel
kernel = np.ones((5, 5), np.uint8)  # 5x5 square kernel

# Apply dilation
dilated_image = cv2.dilate(binary_image, kernel, iterations=1)

# Apply erosion
eroded_image = cv2.erode(binary_image, kernel, iterations=1)

# Display images
cv2.imshow('Original Image', image)
cv2.imshow('Binary Image', binary_image)
cv2.imshow('Dilated Image', dilated_image)
cv2.imshow('Eroded Image', eroded_image)

# Wait and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
