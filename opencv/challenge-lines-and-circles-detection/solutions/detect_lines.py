import cv2
import numpy as np


def detect_lines(image: np.ndarray) -> np.ndarray:
    """
    Detect lines in an image using the HoughLinesP function.

    :param image: The input image (preprocessed)
    :return: A copy of the original image with the detected lines drawn on it
    """
    # Set the required parameters for the HoughLinesP function
    rho = 1
    theta = np.pi / 180
    threshold = 100
    min_line_length = 100
    max_line_gap = 50

    # Binarization is first performed using the Canny edge detection method.
    binary = cv2.Canny(image, 20, 40)

    # Apply the HoughLinesP function to the preprocessed image
    lines = cv2.HoughLinesP(
        binary,
        rho,
        theta,
        threshold,
        minLineLength=min_line_length,
        maxLineGap=max_line_gap,
    )
    return lines
