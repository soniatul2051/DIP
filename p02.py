import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_histogram(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert the image to grayscale if it's not already
    if len(img.shape) == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img

    # Calculate histogram
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

    # Display histogram
    plt.plot(hist, color='gray')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()

if __name__ == "__main__":
    image_path = 'download.jpeg'  # Change this to the path of your image
    display_histogram(image_path)
