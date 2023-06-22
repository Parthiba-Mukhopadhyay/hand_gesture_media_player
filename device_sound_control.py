
import cv2
import mediapipe as mp
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np

vid=cv2.VideoCapture(0) # captures the video

drawing=mp.solutions.drawing_utils #provides options for drawing keypoints and connections on frames
hands=mp.solutions.hands #predefined to detect hand
hand_obj=hands.Hands(max_num_hands=1) # to check for multiple hands in frame and restrict it to 1

devices = AudioUtilities.GetSpeakers() #to setup pycaw
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume)) 

vMin, vMax = volume.GetVolumeRange()[:2] #to get maximum and minimum volume range of device


# while loop runs and captures video frame by frame till termination condition is satisfiied
while True:
  ret,frame = vid.read() # to convert the video in frames. the function returns a tuple that is stored in ret 
  frame=cv2.flip(frame,1) # flips the frame horizontally

  res=hand_obj.process(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))

  if res.multi_hand_landmarks: #condition to check if 1 or more hand is present in the frame
    kplist=res.multi_hand_landmarks[0] # we create a list of the hand landmark keypoints and pass the list to function to perform operations
    
    ll = []
    for id, lm in enumerate(kplist.landmark):
        h, w, c = frame.shape
        cx, cy = int(lm.x * w), int(lm.y * h)
        ll.append([id, cx, cy]) 
    
    drawing.draw_landmarks(frame, res.multi_hand_landmarks[0],hands.HAND_CONNECTIONS) #we select 0 for considering only first element of tuple i.e. considering only 1 hand. Hand connections show the drawn lines between the landmark keypoints

    if ll != []:
      x1, y1 = ll[4][1], ll[4][2]
      x2, y2 = ll[8][1], ll[8][2]

    cv2.circle(frame, (x1, y1), 15, (255, 0, 0), cv2.FILLED)  # to plot circle on thumb
    cv2.circle(frame, (x2, y2), 15, (255, 0, 0), cv2.FILLED)  #to plot circle on index finger
    cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)

    length = hypot(x2 - x1, y2 - y1) #to determine hypotenuse (distance) between the dynamic points
    vol = np.interp(length, [15, 220], [vMin, vMax])
    print(vol, length)
    volume.SetMasterVolumeLevel(vol, None) 

  cv2.imshow('Window',frame) # to show the captured frames to the user through user window

  #to check for termination condition, escape [esc] button code:27
  if cv2.waitKey(1) == 27:
    cv2.destroyAllWindows()
    vid.release()
    break 



