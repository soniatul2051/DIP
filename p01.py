import cv2

def display_grayscale_image(image_path):
    # Read the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image was successfully loaded
    if img is None:
        print("Error: Unable to read the image.")
        return

    # Display the grayscale image
    cv2.imshow('Grayscale Image', img)
    cv2.waitKey(0)  # Wait for any key to be pressed
    cv2.destroyAllWindows()  # Close all OpenCV windows

if __name__ == "__main__":
    image_path = 'download.jpeg'  # Change this to the path of your grayscale image
    display_grayscale_image(image_path)
