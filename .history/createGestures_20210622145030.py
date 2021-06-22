import cv2
import os
import time

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

    for imgnum in range(number_imgs+4):
        ret, frame = cap.read()
        


        if ret:
            frame = cv2.flip(frame,1)
        display = cv2.rectangle(frame.copy(),(200,100),(500,400),(0,255,0),2) 
        cv2.imshow('curFrame',display)
        ROI = frame[100:400, 200:500].copy()
        cv2.imshow('Current Roi', ROI)

        if imgnum == 0 or imgnum == 1 or imgnum == 2 or imgnum == 3:
            continue
        else:
            imgname = os.path.join(IMAGES_PATH, ges_name, '{}.jpg'.format(str(imgnum-3)))
            cv2.imwrite(imgname, ROI)



        time.sleep(2)
    


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    ges_name = input("Enter gesture name: ")

print('DONE...')
    