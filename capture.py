# This project is to capture the web cam footage


import cv2,time


# Create an object for the camera. Zero for the external camera
videoCamera = cv2.VideoCapture(0)


print("OpenCV2")


# Shutdown the camera
videoCamera.release()

