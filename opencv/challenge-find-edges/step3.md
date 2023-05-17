# Fine-Tuning and Saving the Result

In the final sub-challenge, you will learn how to fine-tune the edge detection results and save the final image. This involves adjusting the parameters of the edge detection algorithms and combining their results to create a final output.

## TODO

Please complete the `fine_tune_and_save_result` function in the file `/home/labex/project/fine_tune_and_save_result.py`.

1. Experiment with different parameter values for the Canny and LoG methods to achieve better edge detection results.
2. Combine the Canny and LoG results using the OpenCV `cv2.addWeighted()` function to create a single output image.
3. Save the final output image using the OpenCV `cv2.imwrite()` function.

## example

Take an example to process the target images.

```python
image, blurred_image = read_and_preprocess_image("image_test.jpg")
canny_edges_img, log_edges_img = apply_edge_detection(blurred_image)
combined_edges= fine_tune_and_save_result(image, canny_edges_img, log_edges_img,"combined_edge_image.jpg")
```

A weight of 0.5 is given to both the Canny edge detection processing result and the Laplacian of Gaussian (LoG) edge detection processing result.
The parameter gama is 0.
The image processing results are as follows:

![example_image2](assets/combine_edges_image.jpg)
