
import cv2
import mediapipe as mp
import pyautogui
import time

def countfinger(list):
  count=0 #counts number of fingers raised
  threshold=(list.landmark[0].y*100-list.landmark[9].y*100)/2 # finds the threshold limit, half the dist between lowest grit of middle finger and end of palm
  if (list.landmark[5].y*100-list.landmark[8].y*100)>threshold: # 1st finger
    count+=1
  if (list.landmark[9].y*100-list.landmark[12].y*100)>threshold: # 2nd finger
    count+=1
  if (list.landmark[13].y*100-list.landmark[16].y*100)>threshold: # 3rd finger
    count+=1
  if (list.landmark[17].y*100-list.landmark[20].y*100)>threshold: # 4th finger
    count+=1
  if (list.landmark[5].x*100-list.landmark[4].x*100)>threshold: # thumb {for thub we check x axis because it moves in x direction unlike the rest that moves in y direction}
    count+=1
  return count

vid=cv2.VideoCapture(0) # captures the video

drawing=mp.solutions.drawing_utils #provides options for drawing keypoints and connections on frames
hands=mp.solutions.hands #predefined to detect hand
hand_obj=hands.Hands(max_num_hands=1) # to check for multiple hands in frame and restrict it to 1


prev=-1
start=False

# while loop runs and captures video frame by frame till termination condition is satisfiied
while True:
  endtime=time.time()
  ret,frame = vid.read() # to convert the video in frames. the function returns a tuple that is stored in ret 
  frame=cv2.flip(frame,1) # flips the frame horizontally

  res=hand_obj.process(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))

  if res.multi_hand_landmarks: #condition to check if 1 or more hand is present in the frame
    kplist=res.multi_hand_landmarks[0] # we create a list of the hand landmark keypoints and pass the list to function to perform operations
    cnt=countfinger(kplist)

    if not(prev==cnt):
        
        if not(start):
          starttime=time.time()
          start=True
        elif(endtime-starttime)>0.2: #to give the user a 0.3sec buffer between two hand operations

          if cnt==1:
            pyautogui.press('right') #to move forward
          
          elif cnt==2:
            pyautogui.press('left') #to move backward

          elif cnt==3:
            pyautogui.press('up') #to increase mediaplayer volume

          elif cnt==4:
            pyautogui.press('down') #to reduce mediaplayer volume
          
          elif cnt==5:
            pyautogui.press('space') #pause/play

          prev=cnt
          start=False

    drawing.draw_landmarks(frame, res.multi_hand_landmarks[0],hands.HAND_CONNECTIONS) #we select 0 for considering only first element of tuple i.e. considering only 1 hand. Hand connections show the drawn lines between the landmark keypoints


  cv2.imshow('Window',frame) # to show the captured frames to the user through user window

  #to check for termination condition, escape [esc] button code:27
  if cv2.waitKey(1) == 27:
    cv2.destroyAllWindows()
    vid.release()
    break 



