import cv2
import numpy as np
import random


def apply_opening_and_closing(
    image: np.ndarray,
    kernel_shape: str,
    kernel_size: int,
    opening_iterations: int,
    closing_iterations: int,
) -> np.ndarray:
    """
    Applies opening and closing operations to the input binary image.

    Args:
    image (np.ndarray): The binary image.
    kernel_shape (str): The shape of the structuring element (rectangular, elliptical, or cross).
    kernel_size (int): The size of the structuring element.
    opening_iterations (int): The number of opening iterations to apply.
    closing_iterations (int): The number of closing iterations to apply.

    Returns:
    np.ndarray: The processed image.
    """
    if kernel_shape == "rectangular":
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    elif kernel_shape == "elliptical":
        kernel = cv2.getStructuringElement(
            cv2.MORPH_ELLIPSE, (kernel_size, kernel_size)
        )
    elif kernel_shape == "cross":
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size, kernel_size))

    opened_image = cv2.morphologyEx(
        image, cv2.MORPH_OPEN, kernel, iterations=opening_iterations
    )
    closed_image = cv2.morphologyEx(
        opened_image, cv2.MORPH_CLOSE, kernel, iterations=closing_iterations
    )

    return closed_image
