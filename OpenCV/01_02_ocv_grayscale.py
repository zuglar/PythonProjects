# OpenCV2 képbeolvasás, szürkeárnyalatos konverzió
# OpenCV online dokumentáció: https://docs.opencv.org/

# OpenCV modul definiciók importálása
import  cv2

# Kép beolvasása fájlból szürkeárnyalatosként
img_gray = cv2.imread('OpenCV-logo.png', cv2.IMREAD_GRAYSCALE)

# Képméret kiiratása konzolra
print('img_gray.shape: ', img_gray.shape)

# Kép megjelenitése ablakba
cv2.imshow('img_gray', img_gray)
cv2.waitKey(0)

# Kép beolvasása fájlból szines
img_color = cv2.imread('OpenCV-logo.png', cv2.IMREAD_COLOR)
print('img_color.shape', img_color.shape)
cv2.imshow('img_color', img_color)

cv2.waitKey(0)

img_gray2 = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# Kép megjelenítése ablakban
cv2.imshow('im_gray2', img_gray2)
cv2.waitKey(0)

cv2.destroyAllWindows()