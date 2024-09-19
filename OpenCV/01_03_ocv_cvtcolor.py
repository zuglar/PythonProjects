# OpenCV2 képbeolvasás, színtér konverzió
# OpenCV online dokumentáció: https://docs.opencv.org/4.9.0/de/d25/imgproc_color_conversions.html

# OpenCV modul definíciók importálása
import cv2

# Szines kép beolvasása fájból
img_bgr = cv2.imread('GolyoAlszik_rs.jpg', cv2.IMREAD_COLOR)
print('img_bgr.shape: ', img_bgr.shape)
cv2.imshow('img_bgr', img_bgr)
cv2.waitKey(0)

# Szürkeárnylat
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
print('img_gray.shape: ', img_gray.shape)
cv2.imshow('img_gray', img_gray)
cv2.waitKey(0)

# Szürkéböl "szines"
img_gray2bgr = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
print('img_gray2bgr.shape: ', img_gray2bgr.shape)
cv2.imshow('img_gray2bgr', img_gray2bgr)
cv2.waitKey(0)

# Áttérés Lab szintérbe
img_Lab = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2Lab)
print('img_Lab.shape: ', img_Lab.shape)
cv2.imshow('img_Lab', img_Lab)
cv2.waitKey(0)

# Lab 2 BGR
img_bgr2 = cv2.cvtColor(img_Lab, cv2.COLOR_Lab2BGR)
print('img_bgr2.shape: ', img_bgr2.shape)
cv2.imshow('img_bgr2', img_bgr2)
cv2.waitKey(0)

cv2.destroyAllWindows()