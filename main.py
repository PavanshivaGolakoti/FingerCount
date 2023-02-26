import cv2
from cvzone.HandTrackingModule import HandDetector
detector =HandDetector(detectionCon=0.8,maxHands=3)
video = cv2.VideoCapture(0)
while True:
    ret,frame = video.read()
    hands,img = detector.findHands(frame)
    if hands:
        fingerUp=detector.fingersUp(hands[0])
        print(fingerUp)
        if fingerUp==[0,0,0,0,0]:
            cv2.putText(frame,'Finger Count: 0' , (20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA )
            cv2.putText(frame,'Jumping' , (440,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA )
        if fingerUp.count(1)==1:
            cv2.putText(frame,'Finger Count: 1' , (20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA )
            cv2.putText(frame,'Not jumping' , (440,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA )
        if fingerUp.count(1)==2:
            cv2.putText(frame,'Finger Count: 2' , (20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA )
            cv2.putText(frame,'Not jumping' , (440,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA )
        if fingerUp.count(1)==3:
            cv2.putText(frame,'Finger Count: 3' , (20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA )
            cv2.putText(frame,'Not jumping' , (440,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA )
        if fingerUp.count(1)==4:
            cv2.putText(frame,'Finger Count: 4' , (20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA )
            cv2.putText(frame,'Not jumping' , (440,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA )
        if fingerUp.count(1)==5:
            cv2.putText(frame,'Finger Count: 5' , (20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA )
            cv2.putText(frame,'Not jumping' , (440,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA )

    cv2.imshow("Frame",frame)
    k=cv2.waitKey(1)
    if k==ord('q'): 
        break
video.release()
cv2.destroyAllWindows()
