# OpenCV2 képbeolvasás, megjelenítés és tükrözés
# OpenCV online dokumentáció: https://docs.opencv.org/

# 1. feladat: Végezzük el az alábbi módosításokat az első példaprogramon!
#
#     Az egyes képek megjelenése után legkésőbb 2 másodperc (azaz 2000 ezredmásodperc...) után lépjen a következő eredményre a program!
#     A bemeneti kép és a tükrözött eredmények külön ablakokban jelenjenek meg!


# OpenCV modul definíciók importálása
import cv2
import os
# dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)
# OpenCV verziószám kiíratása
print('OpenCV verzió:', cv2.__version__)

# # Kép beolvasása fájlból
img = cv2.imread('OpenCV-logo.png', cv2.IMREAD_COLOR)

# Képméret kiíratása konzolra
print(img.shape)

# Kép megjelenítése ablakban
cv2.imshow('image', img)
cv2.waitKey(2000)

# Tükrözés a függőleges középtengelyre és megjelenítés
flipped = cv2.flip(img, 1)
cv2.imshow('flipped-image-1', flipped)
cv2.imwrite('OpenCV-logo-flipped.png', flipped)
cv2.waitKey(2000)

# Tükrözés mindkét középtengelyre és megjelenítés
flipped2 = cv2.flip(img, -1)
cv2.imshow('flipped-image-2', flipped2)
cv2.waitKey(2000)

# Összes ablak bezárása
cv2.destroyAllWindows()
