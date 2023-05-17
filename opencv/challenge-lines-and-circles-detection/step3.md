# Circle Detection

In this sub-challenge, you will implement the HoughCircles function to detect circles in the preprocessed image. The HoughCircles function is an implementation of the Hough Transform, adapted for detecting circles in images.

## TODO:

Please complete the detect_circles function in the file `/home/labex/project/detect_circles.py`.

- The Gaussian-filtered image output by the `read_and_preprocess_image.py` function is used as the input value of `detect_circles.py`.
- Set the required parameters for the HoughCircles function.
- Apply the `HoughCircles` function to the preprocessed image.
- Iterate through the detected circles and draw them on a copy of the original image.
- The return result is just the same as the output of `cv2.HoughCircles` function.
