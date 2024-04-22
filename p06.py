import cv2
import numpy as np

def eliminate_high_frequency(image_path, threshold):
    # Read the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Perform Fourier transform
    f_transform = np.fft.fft2(img)
    f_shift = np.fft.fftshift(f_transform)

    # Determine center frequencies
    rows, cols = img.shape
    crow, ccol = rows // 2, cols // 2

    # Zero out high-frequency components beyond the threshold
    f_shift[crow - threshold:crow + threshold, ccol - threshold:ccol + threshold] = 0

    # Perform inverse Fourier transform
    f_ishift = np.fft.ifftshift(f_shift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)

    # Convert to uint8
    img_back = np.uint8(img_back)

    # Display the original and processed images
    cv2.imshow('Original Image', img)
    cv2.imshow('Processed Image (High Frequency Eliminated)', img_back)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = 'download.jpeg'  # Change this to the path of your image
    threshold = 50  # Adjust this threshold to control the elimination of high-frequency components
    eliminate_high_frequency(image_path, threshold)
