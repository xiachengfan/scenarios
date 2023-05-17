import sys

sys.path.append("/home/labex/project")
import inspect
from read_and_preprocess_image import read_and_preprocess_image
import unittest
import numpy as np


class TestOpenCVChallenge(unittest.TestCase):
    def test_read_and_preprocess_image(self):
        preprocessed_image = read_and_preprocess_image("/tmp/image_test.jpg")
        source_lines, _ = inspect.getsourcelines(read_and_preprocess_image)
        targets = ["cv2.GaussianBlur"]
        for target in targets:
            flag = False
            for line in source_lines:
                if target in line:
                    flag = True
                else:
                    pass
            self.assertTrue(flag)
        self.assertIsNotNone(preprocessed_image)
        self.assertEqual(preprocessed_image.shape, (400, 600))


if __name__ == "__main__":
    unittest.main()
