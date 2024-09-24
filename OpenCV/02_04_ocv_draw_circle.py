

# OpenCV2 képmátrix létrehozása, megjelenítése és fájlba mentése
# OpenCV online dokumentáció: https://docs.opencv.org/

# Modul definíciók importálása
import numpy as np
import cv2

# 320x200x3 méretű Numpy tömb létrehozása RGB színes képnek
img = np.ndarray((220, 320,3), np.uint8)
# Feltöltés 192 (világosszürke) színnel
img.fill(192)
# Kör rajzolása az (50, 100) középponttal, 40 sugárral, vörös színnel, kitöltve
cv2.circle(img, (50, 100), 40, (0, 0, 192), -1)

# vonal rajzolás
cv2.line(img, (60, 10), (10, 200), (255, 0, 0), 2)
# elipszis rajzolás
#cv2.ellipse(img,(110, 160),(10, 10 ), 0, 0, 180, (0, 255, 0), 1)
cv2.ellipse(img,(160,110),(100,50),90,90,270  ,(0, 255, 0),-1)
# Sokszög körvonalak és kitöltött sokszögek
contour1 = np.array([[130, 20], [150, 150], [250, 150], [280, 50]])
cv2.fillPoly(img, [contour1], color=(0, 192, 0))
cv2.polylines(img, [contour1], isClosed=False, color=(192, 0, 0), thickness=5)
#Szöveg elhelyezése
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,100), font, 1,(0,0,0),2,cv2.LINE_AA)
# További rajzoló függvények:
#   https://docs.opencv.org/4.5.1/dc/da5/tutorial_py_drawing_functions.html

# Kép megjelenítése ablakban
cv2.imshow('image', img)
cv2.waitKey(0)

# Kép mentése fájlba
cv2.imwrite('ocv_test1_out.png', img)

# Összes ablak bezárása
cv2.destroyAllWindows()

