import cv2

def edge_detection(image_path, operator):
    # Read the image
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply the specified edge detection operator
    if operator == "sobel":
        edges = cv2.Sobel(gray, cv2.CV_64F, 1, 1, ksize=5)
        edges = cv2.convertScaleAbs(edges)  # Convert back to uint8
    elif operator == "prewitt":
        kernelx = cv2.getDerivKernels(1, 0, 3)[0]  # Get the x-axis kernel
        kernely = cv2.getDerivKernels(0, 1, 3)[0]  # Get the y-axis kernel
        edgesx = cv2.filter2D(gray, -1, kernelx)
        edgesy = cv2.filter2D(gray, -1, kernely)
        edges = cv2.magnitude(edgesx, edgesy)
    elif operator == "laplacian":
        edges = cv2.Laplacian(gray, cv2.CV_64F)
        edges = cv2.convertScaleAbs(edges)  # Convert back to uint8
    else:
        print("Invalid operator specified. Please choose 'sobel', 'prewitt', or 'laplacian'.")
        return

    # Display the original image and the edges
    cv2.imshow('Original Image', img)
    cv2.imshow('Edges (' + operator.capitalize() + ' Operator)', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = 'download.jpeg'  # Change this to the path of your image
    edge_detection(image_path, 'sobel')  # Change the operator as needed: sobel, prewitt, or laplacian
