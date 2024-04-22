import cv2
import numpy as np

def discretize_image(image_path, factor):
    # Read the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Perform Fourier transform
    f_transform = np.fft.fft2(img)
    f_shift = np.fft.fftshift(f_transform)

    # Determine center frequencies
    rows, cols = img.shape
    crow, ccol = rows // 2, cols // 2

    # Apply low-pass filter to remove high frequencies
    f_shift[crow - factor:crow + factor, ccol - factor:ccol + factor] = 0

    # Perform inverse Fourier transform
    f_ishift = np.fft.ifftshift(f_shift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)

    # Convert to uint8
    img_back = np.uint8(img_back)

    # Normalize the image
    img_back = cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX)

    # Display the original and discretized images
    cv2.imshow('Original Image', img)
    cv2.imshow('Discretized Image', img_back)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = 'download.jpeg'  # Change this to the path of your image
    factor = 50  # Adjust this factor to control the amount of discretization
    discretize_image(image_path, factor)
