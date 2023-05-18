import cv2
from typing import Tuple


def read_and_preprocess_image(
    image_path: str, kernel_size: Tuple[int, int] = (5, 5)
) -> Tuple:
    """
    Read an image file, convert it to grayscale, and apply Gaussian Blur to reduce noise.

    :param image_path: str, path to the input image file
    :param kernel_size: Tuple[int, int], kernel size for Gaussian Blur, default is (5, 5)
    :return: Tuple containing the original image and preprocessed grayscale image
    """


# TODO: implement this function here.
# Note: Do not change the existing code.
