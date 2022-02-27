# import library
import cv2
from cv2 import resize
from numpy import imag
from sklearn.neighbors import radius_neighbors_graph

# image path
image_path = 'image/1.jpg'

# read the image file
image = cv2.imread(image_path)

# output the image
cv2.imshow("Sample Image", image)

# Save Images
"""filename = 'test_image.png'
cv2.imwrite(filename, image)
print('Done')"""

# Image properties
"""print(image.shape)"""

# Changing Color Space
# RGB -> Gray
"""gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray)"""

# Gray -> RGB
"""rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
cv2.imshow("RGB Image", rgb)"""

# resize the image
"""resize = cv2.resize(image, (100,100))
cv2.imshow("Resize", resize)"""

# Displaying Text
"""text = "This is for testing" 
coordinates = (10,100)
font = cv2.FONT_HERSHEY_SIMPLEX
fontsize = 1
color = (255,0,255)
thickness = 3

textImage = cv2.putText(image, text, coordinates, font, fontsize, color, thickness)
cv2.imshow("Text Image", textImage)
"""

# Drawing a Line
"""start_point = (0,0)
end_point = (100,100)
color = (255, 0, 255)
thickness = 2

lineImage = cv2.line(image, start_point, end_point, color, thickness)
cv2.imshow("line on Image", lineImage)"""

# Drawing a Circle
"""color = (255, 0, 255)
thickness = 2
center = (50, 50)
radius = 40

circleImage = cv2.circle(image, center, radius, color, thickness)
cv2.imshow("Circle", circleImage)"""

# Drawing a rectangle
"""start_point = (50,50)
end_point = (100,100)
color = (255, 0, 255)
thickness = 2

rectangleImage = cv2.rectangle(image, start_point, end_point, color, thickness)
cv2.imshow("Rectangle", rectangleImage)"""

# Drawing an ellipse
"""start_angle = 10
end_angle = 360
center = (100, 100)
radius = 30
axis_length = (100,50)
angle = 30
color = (255, 0, 255)
thickness = 2

ellipseImage = cv2.ellipse(image, center , axis_length, angle, start_angle, end_angle, color, thickness)
cv2.imshow("Ellipse", ellipseImage)"""


# wait for any key to close all the window
cv2.waitKey(0)
cv2.destroyAllWindows()
