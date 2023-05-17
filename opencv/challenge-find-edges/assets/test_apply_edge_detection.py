import sys

sys.path.append("/home/labex/project")

from read_and_preprocess_image import read_and_preprocess_image
from apply_edge_detection import apply_edge_detection
import unittest
import numpy as np


class TestEdgeDetection(unittest.TestCase):
    def test_apply_edge_detection(self):
        image_path = "/tmp/image_test.jpg"
        _, blurred_image = read_and_preprocess_image(image_path)
        canny_edges, log_edges = apply_edge_detection(blurred_image)

        self.assertIsInstance(canny_edges, np.ndarray)
        self.assertIsInstance(log_edges, np.ndarray)
        self.assertEqual(canny_edges.shape, log_edges.shape)
        self.assertTrue((blurred_image != canny_edges).sum())
        self.assertTrue((blurred_image != log_edges).sum())


if __name__ == "__main__":
    unittest.main()
