# from cv2 import imshow
import numpy as np
import cv2

src1 = cv2.imread("image/1.jpg")
src2 = cv2.imread("image/2.jpg")

image1 = cv2.resize(src1, (300, 300))
image2 = cv2.resize(src2, (300, 300))

blendImg = cv2.addWeighted(image1, 0.5, image2, 1,1)
cv2.imshow('Testing', blendImg)
cv2.waitKey(0)
cv2.destroyAllWindows()