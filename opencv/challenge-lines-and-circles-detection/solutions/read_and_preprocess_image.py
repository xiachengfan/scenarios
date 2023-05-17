import cv2
import numpy as np


def read_and_preprocess_image(image_path: str) -> np.ndarray:
    """
    Read and preprocess an input image.

    :param image_path: The path of the input image file
    :return: The preprocessed image (grayscale and Gaussian blurred)
    """
    # Read the input image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to the image
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    return blurred_image
