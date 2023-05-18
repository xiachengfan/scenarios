import sys

sys.path.append("/home/labex/project")

from read_and_preprocess_image import read_and_preprocess_image
import unittest
import numpy as np
import cv2


class TestEdgeDetection(unittest.TestCase):
    def test_read_and_preprocess_image(self):
        image_path = "/tmp/image_test.jpg"
        image, blurred_image = read_and_preprocess_image(image_path, (5, 5))
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        self.assertIsInstance(image, np.ndarray)
        self.assertIsInstance(blurred_image, np.ndarray)
        self.assertEqual(image.shape[:2], blurred_image.shape)
        self.assertEqual(len(blurred_image.shape), 2)
        self.assertTrue((gray_image != blurred_image).sum())


if __name__ == "__main__":
    unittest.main()
