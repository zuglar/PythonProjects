# OpenCV2 képbeolvasás, megjelenítés és tükrözés
# OpenCV online dokumentáció: https://docs.opencv.org/
from xmlrpc.client import Boolean

# 5. feladat: Készítsünk animált megjelenítést!
#
#     A program másodpercenként váltogatva tükrözze a képet, amíg a Q vagy az ESC billentyű lenyomásával ki nem lépünk a ciklusból!

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
h_flip = True
while True:
    key = cv2.waitKeyEx(1000)
    if key == -1:
        if h_flip:
            img = cv2.flip(img, 0)
            h_flip = False
        else:
            img = cv2.flip(img, 1)
            h_flip = True

    if key == 27 or key == 113:
        break

    cv2.imshow('image', img)

    print('Lenyomott billentyű és kódja:', key)
# key = cv2.waitKey(0)
#
# # Tükrözés a függőleges középtengelyre és megjelenítés
# flipped = cv2.flip(img, 1)
# cv2.imshow('image', flipped)
# cv2.imwrite('OpenCV-logo-flipped.png', flipped)
# cv2.waitKey(0)
#
# # Tükrözés mindkét középtengelyre és megjelenítés
# flipped2 = cv2.flip(img, -1)
# cv2.imshow('image', flipped2)
# cv2.waitKey(0)
#
# Összes ablak bezárása
cv2.destroyAllWindows()
