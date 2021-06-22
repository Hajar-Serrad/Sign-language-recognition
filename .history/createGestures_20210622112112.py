#  img = cv2.rectangle(frame, (425, 100), (625, 300), (0, 255, 0), thickness=2, lineType=8, shift=0)

#            lower_blue = np.array([l_h, l_s, l_v])
 #           upper_blue = np.array([u_h, u_s, u_v])
  #          imcrop = img[102:298, 427:623]
   #         hsv = cv2.cvtColor(imcrop, cv2.COLOR_BGR2HSV)
    #        mask = cv2.inRange(hsv, lower_blue, upper_blue)

     #       result = cv2.bitwise_and(imcrop, imcrop, mask=mask)

import cv2
import os
import time
import uuid

IMAGES_PATH = 'Dataset\'

labels = ['hello', 'thanks', 'yes', 'no', 'iloveyou']
number_ings = 15

for label in labels:
    !mkdir {'Dataset\\'+label}
    cap = cv2.VideoCapture(0)
    