import cv2
import numpy as np
import os

dir_to_crop = 'cnh_a'

for filename in os.listdir(dir_to_crop):
#Load the image
    IMG = cv2.imread(dir_to_crop + '/' + filename)

#Create a grayscale version of the image and apply a bilateralFilter to it.
    GRAY = cv2.cvtColor(IMG, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('cvtColor Result:', GRAY)
    #cv2.waitKey(0)

    GRAY = cv2.bilateralFilter(GRAY, 11, 17, 17)
    #cv2.imshow('bilateralFilter Result:', GRAY)
    #cv2.waitKey(0)

#Instantiate a Kernel to apply erosion to the image.
    KERNEL = np.ones((5, 5), np.uint8)
    EROSION = cv2.erode(GRAY, KERNEL, iterations=2)
    #cv2.imshow('erode Result:', EROSION)
    #cv2.waitKey(0)

#Instantiate a Kernel to apply dilate to the image.
    KERNEL = np.ones((4, 4), np.uint8)
    DILATION = cv2.dilate(EROSION, KERNEL, iterations=2)
    #cv2.imshow('dilate Result:', EROSION)
    #cv2.waitKey(0)

    edged = cv2.Canny(DILATION, 30, 200)
    #cv2.imshow('Canny Result:', edged)
    #cv2.waitKey(0)

    _, contours, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    rects = [cv2.boundingRect(cnt) for cnt in contours]
    rects = sorted(rects,key=lambda  x:x[1],reverse=True)

    j = 1
    y_old = 5000
    x_old = 5000

    biggest_rects = sorted(rects, key=lambda rect: rect[2] * rect[3], reverse=True )[:2]

    for rect in biggest_rects:
        x, y, w, h = rect

        area = w * h

        print('rect area: ' + str(area))
        out = IMG[y+10:y+h-10,x+10:x+w-10]

        cv2.imwrite(filename+ '_' + str(j) + '.jpg', out)
        print('Test image crop')
        #cv2.imshow('TESTANO', out)
        #cv2.waitKey(0)
        j+=1
