# Reading a Video and Saving a Frame

To capture a video, you need to create a `VideoCapture` object. Here's an example of reading a video and saving each frame to the `frame` folder:

Video path is `/home/labex/project/video.mp4`

File path is `/home/labex/project/read_video.py`

Open the `read_video.py` file. Then input the following code.

```python
import cv2
import os

# Check if the 'frame' folder exists. Create it if it doesn't.
folder = os.path.exists('frame')
if not folder:
	os.makedirs('frame')
	print('new folder...')
	print('OK')
else:
	print('There is this folder!')

# Frame number
number = 0

# Create a VideoCapture object
cap = cv2.VideoCapture('video.mp4')

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Frame number added
    number = number + 1
    if ret:
        # Save the frame
        cv2.imwrite(f"./frame/save{number}.jpg", frame)

    # Exit the loop
    else:
        break

print('Each frame has been saved to the frame folder')

print('Video read successfully!')

# Release the VideoCapture object
cap.release()
```

In this example, we create a `VideoCapture` object by passing the path to the video file we want to read. We then use a `while` loop to read each frame of the video using the `read()` method. If the frame is successfully read, we use the `imwrite()` method to save the frame. Finally, we release the `VideoCapture` object.

You can run the following command in the terminal to execute.

```bash
python /home/labex/project/read_video.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Afterward, wait for Terminal to output "Video read successfully!" and you will see the pictures of each frame in the frame folder.
