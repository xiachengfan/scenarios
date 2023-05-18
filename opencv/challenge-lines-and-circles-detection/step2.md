# Line Detection

In this sub-challenge, you will implement the HoughLinesP function to detect lines in the preprocessed image. The HoughLinesP function is a probabilistic implementation of the Hough Transform, a technique used for detecting lines in images.

## TODO:

Please complete the detect_lines function in the file `/home/labex/project/detect_lines.py`.

- The Gaussian-filtered image output by the `read_and_preprocess_image.py` function is used as the input value of `detect_lines.py`.
- There are more false detections when detecting lines than when detecting circles. Binarizing the input image using the Canny edge detection method `cv2.Canny` can effectively solve this problem.
- Set the required parameters for the HoughLinesP function.
- Apply the `HoughLinesP` function to the preprocessed image.
- Iterate through the detected lines and draw them on a copy of the original image.
- The return result is just the same as the output of the `cv2.HoughLinesP` function.
