#import cv2
#vc = cv2.VideoCapture('test.mp4')
#if vc.isOpened():
#    open,frame = vc.read()
#else:
#    open = False

#while open:
#    ret,frame=vc.read()
#    if frame is None:
#        break
#    if ret ==True:
#        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#        cv2.imshow('result',gray)
#        if cv2.waitKey(100) & 0xff ==27:
#            break
#vc.release()
#cv2.destroyAllWindows()


import cv2

capture = cv2.VideoCapture(0) #调用电脑摄像头
if capture.isOpened():
    open,frame = capture.read()
else:
    open = False

while open:
    ret,frame = capture.read()
    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray',gray)
        if cv2.waitKey(50) & 0xff ==27:
            break
    else:
        break
capture.release()
cv2.destroyAllWindows()