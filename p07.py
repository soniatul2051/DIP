import cv2
import numpy as np

def create_color_image(width, height):
    # Create a blank image with the specified width and height
    color_image = np.zeros((height, width, 3), dtype=np.uint8)

    # Fill the image with a color (here, I'm filling it with blue)
    color_image[:, :] = (255, 0, 0)  # Blue color in BGR format

    return color_image

def display_image(image):
    # Display the image
    cv2.imshow('Color Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def read_image(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Check if the image was successfully loaded
    if image is None:
        print("Error: Unable to read the image.")
        return

    return image

def write_image(image, output_path):
    # Write the image to the specified output path
    cv2.imwrite(output_path, image)
    print("Image saved successfully.")

if __name__ == "__main__":
    # Create a color image with specified width and height
    width = 400
    height = 300
    color_image = create_color_image(width, height)

    # Display the color image
    display_image(color_image)

    # Save the color image to disk
    output_path = 'color_image.jpg'
    write_image(color_image, output_path)

    # Read the color image from disk
    read_image(output_path)
