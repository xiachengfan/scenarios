import sys

sys.path.append("/home/labex/project")
from read_and_preprocess_image import read_and_preprocess_image
from detect_lines import detect_lines
import inspect
import unittest
import numpy as np


class TestOpenCVChallenge(unittest.TestCase):
    def test_detect_lines(self):
        preprocessed_image = read_and_preprocess_image("/tmp/image_test.jpg")
        line_detection_result = detect_lines(preprocessed_image)
        flag1 = True
        if type(line_detection_result) == np.ndarray or line_detection_result == None:
            pass
        else:
            flag1 = False
        self.assertTrue(flag1)

        source_lines, _ = inspect.getsourcelines(detect_lines)
        targets = ["cv2.Canny", "cv2.HoughLinesP"]
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
