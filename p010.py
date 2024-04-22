import cv2
import numpy as np

def segment_image(image_path):
    # Read the image
    img = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to obtain a binary image
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Perform morphological operations to remove noise and fill gaps
    kernel = np.ones((3,3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
    
    # Find sure background area
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    
    # Find sure foreground area
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
    
    # Find unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)
    
    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)
    
    # Add one to all labels so that sure background is not 0, but 1
    markers = markers + 1
    
    # Mark unknown region with 0
    markers[unknown == 255] = 0
    
    # Apply watershed algorithm
    markers = cv2.watershed(img, markers)
    
    # Outline the segmented regions
    img[markers == -1] = [255,0,0]  # Mark watershed boundaries in blue
    
    # Display the segmented image
    cv2.imshow('Segmented Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = 'download.jpeg'  # Change this to the path of your image
    segment_image(image_path)
