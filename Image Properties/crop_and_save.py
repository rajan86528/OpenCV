# from cv2 import imshow
import numpy as np
import cv2

image = cv2.imread("image/1.jpg")

roi = cv2.selectROI(image)

print(roi)
crop = image[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]) :int(roi[0]+roi[2])]
cv2.imshow("Roi Image", crop)
cv2.imwrite("Crop.jpg", crop)


# cv2.imshow('Testing', image)
cv2.waitKey(0)
cv2.destroyAllWindows()