import cv2
import numpy as np


def draw_lines_and_circles(
    image: np.ndarray, lines: np.ndarray, circles: np.ndarray
) -> np.ndarray:
    """
    Draw detected lines and circles on the original image.

    :param image: The input image (preprocessed)
    :param lines: The detected lines
    :param circles: The detected circles
    :return: A copy of the original image
    """

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for circle in circles[0, :]:
            center = (circle[0], circle[1])
            radius = circle[2]
            cv2.circle(image, center, radius, (0, 255, 0), 2)

    return image
