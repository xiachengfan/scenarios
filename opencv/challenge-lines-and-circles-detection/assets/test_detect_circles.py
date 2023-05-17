import sys

sys.path.append("/home/labex/project")
import inspect
from read_and_preprocess_image import read_and_preprocess_image
from detect_circles import detect_circles
import unittest
import numpy as np


class TestOpenCVChallenge(unittest.TestCase):
    def test_detect_circles(self):
        preprocessed_image = read_and_preprocess_image("/tmp/image_test.jpg")
        circle_detection_result = detect_circles(preprocessed_image)
        flag1 = True
        if (
            type(circle_detection_result) == np.ndarray
            or circle_detection_result == None
        ):
            pass
        else:
            flag1 = False
        self.assertTrue(flag1)

        source_lines, _ = inspect.getsourcelines(detect_circles)
        targets = ["cv2.HoughCircles"]
        for target in targets:
            flag2 = False
            for line in source_lines:
                if target in line:
                    flag2 = True
                else:
                    pass
            self.assertTrue(flag2)


if __name__ == "__main__":
    unittest.main()
