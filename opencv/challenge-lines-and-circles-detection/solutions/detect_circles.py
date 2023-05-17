import cv2
import numpy as np


def detect_circles(image: np.ndarray) -> np.ndarray:
    """
    Detect circles in an image using the HoughCircles function.

    :param image: The input image (preprocessed)
    :return: A copy of the original image with the detected circles drawn on it
    """
    # Set the required parameters for the HoughCircles function
    dp = 1
    min_dist = 50
    param1 = 100
    param2 = 30
    min_radius = 10
    max_radius = 100

    # Apply the HoughCircles function to the preprocessed image
    circles = cv2.HoughCircles(
        image,
        cv2.HOUGH_GRADIENT,
        dp,
        min_dist,
        param1=param1,
        param2=param2,
        minRadius=min_radius,
        maxRadius=max_radius,
    )
    return circles
