import cv2
import numpy as np

def get_color_values(image_path, x, y):
    # Read the image
    image = cv2.imread(image_path)

    # Check if the image was successfully loaded
    if image is None:
        print("Error: Unable to read the image.")
        return

    # Extract the BGR color values at the specified (x, y) coordinates
    b, g, r = image[y, x]

    # Display the BGR color values
    print("BGR values at ({}, {}):".format(x, y))
    print("Blue: {}".format(b))
    print("Green: {}".format(g))
    print("Red: {}".format(r))

    # Resolve the color value from BGR to human-readable format
    color = np.uint8([[[b, g, r]]])
    hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
    hue, saturation, value = hsv_color[0][0]

    # Display the resolved color value in HSV format
    print("\nResolved color value (HSV) at ({}, {}):".format(x, y))
    print("Hue: {}".format(hue))
    print("Saturation: {}".format(saturation))
    print("Value: {}".format(value))

if __name__ == "__main__":
    # Path to the image
    image_path = 'download.jpeg'

    # Coordinates of the color box (choose any point within the color box)
    x = 100
    y = 50

    # Get the color values from the image
    get_color_values(image_path, x, y)

