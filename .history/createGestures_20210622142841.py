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

number_imgs = 15 # to edit
ges_name = input("Enter gesture name: ")

while ges_name!='/':
    
    if not os.path.exists('Dataset\\' + ges_name):
        os.mkdir('Dataset\\' + ges_name)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print ("Could not open cam")
        exit()

    print('Collecting images for {}'.format(ges_name))
    time.sleep(3)

    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        


        if ret:
            frame = cv2.flip(frame,1)
        display = cv2.rectangle(frame.copy(),(200,100),(500,400),(0,255,0),2) 
        cv2.imshow('curFrame',display)
        ROI = frame[100:400, 200:500].copy()
        cv2.imshow('Current Roi', ROI)

        imgname = os.path.join(IMAGES_PATH, ges_name, '{}.jpg'.format(str(imgnum+1)))
        cv2.imwrite(imgname, ROI)



        time.sleep(2)
    


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    ges_name = input("Enter gesture name: ")

print('DONE...')
    