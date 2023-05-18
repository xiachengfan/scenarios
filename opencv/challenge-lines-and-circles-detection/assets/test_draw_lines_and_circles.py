import sys

sys.path.append("/home/labex/project")
import inspect
from read_and_preprocess_image import read_and_preprocess_image
from draw_lines_and_circles import draw_lines_and_circles
import unittest
import numpy as np


class TestOpenCVChallenge(unittest.TestCase):
    def test_draw_lines_and_circles(self):
        preprocessed_image = read_and_preprocess_image("/tmp/image_test.jpg")
        lines = np.array([[[10, 10, 20, 20]]])
        circles = np.array([[[20, 20, 5]]])
        result_image = draw_lines_and_circles(preprocessed_image, lines, circles)
        flag1 = True
        if type(result_image) == np.ndarray or result_image == None:
            pass
        else:
            flag1 = False
        self.assertTrue(flag1)

        source_lines, _ = inspect.getsourcelines(draw_lines_and_circles)
        targets = ["cv2.line", "cv2.circle"]
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
