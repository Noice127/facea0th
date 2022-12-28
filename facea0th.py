from deepface import DeepFace
from cv2 import *
import cv2
import time


cam_port = 0
cam = cv2.VideoCapture(cam_port)
  

def face_lock(imgPath1 = "face.png"):
    while True:
        # reading the input using the camera
        result, image = cam.read()

        cv2.imshow('my webcam', image)
        if cv2.waitKey(1) == ord("e"): 
            # If image will detected without any error, 
            # show result
            if result:
        
            # showing result, it take frame name and image 
            # output
                cv2.imshow("Picture", image)
                time.sleep(3)
            # saving image in local storage
                cv2.imwrite(imgPath1, image)
                time.sleep(3)

        # If keyboard interrupt occurs, destroy image 
            # window
                cv2.waitKey(0)
                cv2.destroyWindow("Picture")
        # If captured image is corrupted, moving to else part
            else:
                print("No image detected. Please! try again")
                





def face_verify(imgPath2):
    
    while True:
        # reading the input using the camera
        result, image = cam.read()

        cv2.imshow('my webcam', image)
        if cv2.waitKey(1) == ord("e"): 
            # If image will detected without any error, 
            # show result
            if result:
        
            # showing result, it take frame name and image 
            # output
                cv2.imshow("Picture", image)
                time.sleep(3)
            # saving image in local storage
                cv2.imwrite(imgPath2, image)
                time.sleep(3)
                result = DeepFace.verify(img1_path = "face.png", img2_path = imgPath2)
                print(result)
        # If keyboard interrupt occurs, destroy image 
            # window
                cv2.waitKey(0)
                cv2.destroyWindow("Picture")
        # If captured image is corrupted, moving to else part
            else:
                print("No image detected. Please! try again")
            

            
