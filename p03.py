import cv2

def edge_detection(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    # Detect edges using Canny edge detector
    edges = cv2.Canny(blurred, 30, 100)  # You can adjust these threshold values

    # Display the original image and the edges
    cv2.imshow('Original Image', img)
    cv2.imshow('Edges', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = 'download.jpeg'  # Change this to the path of your image
    edge_detection(image_path)
