import sys

sys.path.append("/home/labex/project")

from read_and_preprocess_image import read_and_preprocess_image
from fine_tune_and_save_result import fine_tune_and_save_result
from apply_edge_detection import apply_edge_detection
import unittest
import cv2
import numpy as np


class TestEdgeDetection(unittest.TestCase):
    def test_fine_tune_and_save_result(self):
        image_path = "/tmp/image_test.jpg"
        output_path = "/tmp/image_test2.jpg"

        image, blurred_image = read_and_preprocess_image(image_path)
        canny_edges, log_edges = apply_edge_detection(blurred_image)

        fine_tune_and_save_result(image, canny_edges, log_edges, output_path)

        saved_image = cv2.imread(output_path)
        self.assertIsInstance(saved_image, np.ndarray)
        self.assertEqual(canny_edges.shape, saved_image.shape[:2])
        self.assertTrue((saved_image != image).sum())


if __name__ == "__main__":
    unittest.main()
