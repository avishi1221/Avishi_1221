import cv2
import numpy as np

# Path to your image
image_path = 'C:/Users/Admin/Desktop/ramp detection/ramp.v3i.yolov5pytorch/train/images/IMG_5332-20230809-220505-_JPG.rf.7aeca5670c68a42fe9095444b4eeb5aa.jpg'

# Load the image
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found.")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Apply Canny edge detection
    edges = cv2.Canny(blurred_image, 50, 150)

    # Find contours from the edges
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a copy of the original image to draw contours
    output_image = image.copy()

    # Draw contours on the image
    cv2.drawContours(output_image, contours, -1, (0, 255, 0), 2)  # Green contours

    # Display the results
    cv2.imshow('Edges of the Ramp', edges)
    cv2.imshow('Detected Edges with Contours', output_image)

    # Wait until a key is pressed and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()












