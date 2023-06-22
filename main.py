#import the necessary packages
#cv2 for enabling camera and using computer vision library
#mediapipe by to access vision parameters for hand detection and point mapping

import cv2
import mediapipe as mp

vid=cv2.VideoCapture(0) # captures the video

# while loop runs and captures video frame by frame till termination condition is satisfiied
while True:
  ret,frame = vid.read() # to convert the video in frames. the function returns a tuple that is stored in ret 
  cv2.imshow('Window',frame) # to show the captured frames to the user through user window

  #to check for termination condition, escape button code:27
  if cv2.waitKey(1) == 27:
    cv2.destroyAllWindows()
    vid.release()
    break 



