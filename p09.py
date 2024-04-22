import cv2
import numpy as np
import pywt

def dwt_image(image_path, wavelet='haar', level=1):
    # Read the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print("Error: Could not read the image. Please check the image path.")
        return

    # Perform 2D DWT
    coeffs = pywt.wavedec2(img, wavelet, level=level)

    # Reconstruct the image using inverse DWT
    reconstructed_img = pywt.waverec2(coeffs, wavelet)

    # Handle possible NaN values from DWT and normalize
    if np.any(np.isnan(reconstructed_img)):
        reconstructed_img = np.nan_to_num(reconstructed_img, nan=0)

    reconstructed_img = cv2.normalize(reconstructed_img, None, 0, 255, cv2.NORM_MINMAX)
    reconstructed_img = np.uint8(reconstructed_img)

    # Display the original and reconstructed images
    cv2.imshow('Original Image', img)
    cv2.imshow('Reconstructed Image (DWT)', reconstructed_img)

    # Wait for any key press to close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the reconstructed image to a file (optional)
    cv2.imwrite("reconstructed_image.png", reconstructed_img)

if __name__ == "__main__":
    image_path = 'download.jpeg'  # Update this to the path of your image
    wavelet = 'haar'  # Wavelet type
    level = 1  # Level of decomposition

    dwt_image(image_path, wavelet, level)
