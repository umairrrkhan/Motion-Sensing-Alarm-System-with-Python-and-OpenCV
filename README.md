# Motion-Sensing Alarm System with Python and OpenCV

- This project uses a webcam and OpenCV to detect motion and trigger an alarm.

## Overview

- The code initializes a webcam video stream, captures frames, converts them to grayscale, and applies Gaussian blurring. It compares the current frame to the 
  previous frame to compute absolute difference and then thresholds this frame delta to detect significant changes.

- If a threshold number of changed pixels are detected, it indicates motion so the code triggers a threaded alarm function that sounds an alarm tone using 
  winsound.

- The result is a basic motion sensing alarm that can detect movement in the webcam's field of view and activate an audible alarm when motion is detected.

## Usage

Clone the repository:

```bash
git clone https://github.com/umairrrkhan/Motion-Sensing-Alarm-System-with-Python-and-OpenCV
```

- Install requirements:

```bash
pip install opencv-python imutils winsound
```

- Run the script:

```bash
python main.py
```

- The webcam feed will open. When significant motion is detected, the audible alarm tone will sound.

- Press q to quit.

## Customizing

- The motion detection sensitivity can be adjusted by modifying the white_pix threshold. Higher values make it less sensitive.

- The alarm tone can be changed by passing different frequency and duration values to winsound.Beep().

## Image

![image](https://www.dropbox.com/s/ew1r4t41tgeoooy/Screenshot%20%2897%29.png?raw=1)

![image](https://www.dropbox.com/s/2yr78pfxu3cwx5f/Screenshot%20%2898%29.png?raw=1)

- OpenCV (https://opencv.org/) - For computer vision and video processing
- imutils (https://github.com/jrosebr1/imutils) - For image resizing
- winsound (https://docs.python.org/3/library/winsound.html) - For playing alarm tones

## Contact

- Email: umairh1819@gmail.com
