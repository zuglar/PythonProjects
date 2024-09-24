# Töltsünk be egy meglévő képet és annotáljuk geometriai elemekkel!

import numpy as np
import cv2

img = cv2.imread('GolyoAlszik_rs.jpg')
print(img.shape)

# line
cv2.line(img, (0, 0), (581, 304), (0, 0, 0), 2, cv2.LINE_4)
# circle
cv2.circle(img, (50, 50), 30, (0, 255, 255), -1)
cv2.circle(img, (50, 50), 30, (255, 0, 0), 2)
# rectangle
cv2.rectangle(img, (431, 154), (578, 299), (0, 0, 255), 3)
# ellipse
cv2.ellipse(img, (290, 152), (150, 100), 0, 0, 360, (255, 255, 0), 4)
# polygon
polygon1 = np.array([[410, 10], [560, 20], [550, 100], [450, 200]])
cv2.fillPoly(img, [polygon1], (255, 255, 255))

polygon2 = np.array([[100, 50], [50, 100], [250, 110], [300, 80]])
cv2.polylines(img, [polygon2], isClosed=False, color=(192, 0, 0), thickness=5)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()