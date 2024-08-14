import cv2
import numpy as np

# Load image
image_path = r"C:\Users\Admin\Desktop\other try cones v5\Data Augmentaded - Cone dataset.v1i.yolov5pytorch\train\images\4_z8126b7d060d92d74599e0618_f101fe32fb4e42534_d20161222_m170753_c001_v0001036_t0051_png.rf.783a326afebcc6b0a504da4f7cf13142.jpg"
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply reverse thresholding
threshold_value = 127
_, binary_mask = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY_INV)

# Convert original image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define HSV ranges for different colors
color_ranges = {
    'orange': (np.array([5, 100, 100]), np.array([15, 255, 255])),
    'red': (np.array([0, 100, 100]), np.array([10, 255, 255])),
    'yellow': (np.array([20, 100, 100]), np.array([30, 255, 255]))
}

# Create a mask for each color and combine them
combined_color_mask = np.zeros_like(gray_image)
for lower, upper in color_ranges.values():
    color_mask = cv2.inRange(hsv_image, lower, upper)
    combined_color_mask = cv2.bitwise_or(combined_color_mask, color_mask)

# Combine the binary mask with the color mask
combined_mask = cv2.bitwise_and(binary_mask, combined_color_mask)

# Create a blurred background
blurred_background = cv2.GaussianBlur(image, (7, 7), 0)

# Enhance visibility of detected cones
highlighted_cones = cv2.bitwise_and(image, image, mask=combined_mask)
highlighted_cones = cv2.addWeighted(highlighted_cones, 2.0, np.zeros_like(image), 0, 0)  # Increase contrast

# Find contours and draw more precise borders
contours, _ = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
bordered_cones = image.copy()

# Draw contours with a thicker line and apply smoothing
for contour in contours:
    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    cv2.drawContours(bordered_cones, [approx], -1, (0, 0, 255), 3)  # Red border

# Create an output image with the highlighted cones and blurred background
result_image = np.where(combined_mask[:, :, None] == 255, highlighted_cones, blurred_background)

# Convert masks to black and white for visualization
combined_mask_bw = cv2.cvtColor(combined_mask, cv2.COLOR_GRAY2BGR)

# Display images
# cv2.imshow('Original Image', image)
# cv2.imshow('Binary Mask', binary_mask)
# cv2.imshow('Color Mask', combined_color_mask)
# cv2.imshow('Combined Mask', combined_mask_bw)
# cv2.imshow('Highlighted Cones', highlighted_cones)
# cv2.imshow('Borders Around Cones', bordered_cones)
cv2.imshow('Detected Cones with Blurred Background', result_image)

# Wait and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
