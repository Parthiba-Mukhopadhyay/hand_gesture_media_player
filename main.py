#import the necessary packages
#cv2 for enabling camera and using computer vision library
#mediapipe by to access vision parameters for hand detection and point mapping

import cv2
import mediapipe as mp

vid=cv2.VideoCapture(0) # captures the video

drawing=mp.solutions.drawing_utils #provides options for drawing keypoints and connections on frames
hands=mp.solutions.hands #predefined to detect hand
hand_obj=hands.Hands(max_num_hands=1) # to check for multiple hands in frame and restrict it to 1

# while loop runs and captures video frame by frame till termination condition is satisfiied
while True:
  ret,frame = vid.read() # to convert the video in frames. the function returns a tuple that is stored in ret 
  frame=cv2.flip(frame,1) # flips the frame horizontally

  res=hand_obj.process(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))

  if res.multi_hand_landmarks: #condition to check if 1 or more hand is present in the frame
    drawing.draw_landmarks(frame, res.multi_hand_landmarks[0],hands.HAND_CONNECTIONS) #we select 0 for considering only first element of tuple i.e. considering only 1 hand. Hand connections show the drawn lines between the landmark keypoints


  cv2.imshow('Window',frame) # to show the captured frames to the user through user window

  #to check for termination condition, escape [esc] button code:27
  if cv2.waitKey(1) == 27:
    cv2.destroyAllWindows()
    vid.release()
    break 



