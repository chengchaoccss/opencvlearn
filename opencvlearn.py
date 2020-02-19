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


#import cv2

#capture = cv2.VideoCapture(0) #调用电脑摄像头
#if capture.isOpened():
#    open,frame = capture.read()
#else:
#    open = False

#while open:
#    ret,frame = capture.read()
#    if ret == True:
#        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#        cv2.imshow('gray',gray)
#        if cv2.waitKey(50) & 0xff ==27:
#            break
#    else:
#        break
#capture.release()
#cv2.destroyAllWindows()


#import cv2
#img= cv2.imread("cat.jpg")
#top,bottom,left,right=(100,100,100,100)
#replicate = cv2.copyMakeBorder(img,top,bottom,left,right,borderType=cv2.BORDER_REPLICATE)
#cv2.imshow("img",replicate)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#reflect = cv2.copyMakeBorder(img,top,bottom,left,right,borderType=cv2.BORDER_REFLECT_101)
#cv2.imshow('reflect',reflect)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#reflect = cv2.copyMakeBorder(img,top,bottom,left,right,cv2.BORDER_CONSTANT,value=12)
#cv2.imshow('reflect',reflect)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


import cv2
img1 = cv2.imread("cat.jpg")
print(img1.shape)
img2 = cv2.imread("dog.jpg")
print(img2.shape)
img2 = cv2.resize(img2,(500,414))
print(img2.shape)
newimg= img1+img2
res = cv2.addWeighted(img1,0.6,img2,0.4,50) #图片按权重融合
res2 = cv2.addWeighted(img1,0.6,img2,0.4,0)
cv2.imshow('0',res2)
cv2.imshow('50',res)
cv2.waitKey(0)
cv2.destroyAllWindows()




import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('cat.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('graycat',img_gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#图像阈值
#第一中：二值
ret,thresh1 = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
# cv2.imshow('thresh1',thresh1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print(ret)

#常用阈值
ret2,thresh2 = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY_INV)
ret3,thresh3 = cv2.threshold(img_gray,127,255,cv2.THRESH_TRUNC)
ret4,thresh4 = cv2.threshold(img_gray,127,255,cv2.THRESH_TOZERO)
ret5,thresh5 = cv2.threshold(img_gray,127,255,cv2.THRESH_TOZERO_INV)
# res = np.hstack((thresh1,thresh2,thresh3,thresh4,thresh5))
# cv2.imshow('thresh',thresh5)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# title = ['img','binary','binary_inv','trunc','tozero','tozero_inv']
# img = [img,thresh1,thresh2,thresh3,thresh4,thresh5]
#
# for i in range(6):
#     plt.subplot(2,3,i+1)
#     plt.imshow(img[i],'gray')
#     plt.xticks([])
#     plt.yticks([])
#     plt.title(title[i])
# plt.show()

#图像滤波平滑处理
#均值滤波
img = cv2.imread('lenaNoise.png')
# img_blur = cv2.blur(img,(3,3))
# cv2.imshow('blue',img_blur)

#方框滤波
# img_boxfilter = cv2.boxFilter(img,-1,(3,3),normalize=True)
# cv2.imshow('boxfilter',img_boxfilter)

#中值滤波
# img_medium = cv2.medianBlur(img,5)
# cv2.imshow('medianblur',img_medium)

#高斯滤波
img_gaussian = cv2.GaussianBlur(img,(3,3),1)
cv2.imshow('imggaussianblur',img_gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()
