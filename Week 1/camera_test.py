import numpy as np
import cv2

# Title: Getting Started with Videos 
# Date: 2019
# Availability: https://docs.opencv.org/3.0beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html

# The code below is utilized from the link above. I have made changes
# to convert the BGR (Blue / Green / Red) to HSV (Hue / Saturation / Value)
# I also commented the code and made it exit after pressing the space key.

cap = cv2.VideoCapture(0)

while(True):
    # Captures video frame-by-frame
    ret, frame = cap.read()

    # Operation on the frame
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Display the resulting frame
    cv2.imshow('frame',hsv)

# Kills the video when space is pressed
    if cv2.waitKey(1) & 0xFF == ord(' '): #ord returns ASCII value of character
        break

# Finally, release the capture
cap.release()
cv2.destroyAllWindows()