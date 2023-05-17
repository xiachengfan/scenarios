import cv2
import numpy as np
import random


def apply_morphological_gradient(
    image: np.ndarray, kernel_shape: str, kernel_size: int
) -> np.ndarray:
    """
    Applies a morphological gradient operation to the input binary image.

    Args:
    image (np.ndarray): The binary image.
    kernel_shape (str): The shape of the structuring element (rectangular, elliptical, or cross).
    kernel_size (int): The size of the structuring element.

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

    gradient_image = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

    return gradient_image
