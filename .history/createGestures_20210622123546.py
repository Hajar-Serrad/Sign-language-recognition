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

IMAGES_PATH = 'Dataset'

labels = ['hello', 'thanks']
number_imgs = 15 # to edit
ges_name = input("Enter gesture name: ")

while ges_name!='/':
    
    if not os.path.exists('Dataset\\' + ges_name):
        os.mkdir('Dataset\\' + ges_name)
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(ges_name))
    time.sleep(5)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH, ges_name, '{}.jpg'.format(str(imgnum)))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)
    


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    ges_name = input("Enter gesture name: ")

print('DONE...')
    