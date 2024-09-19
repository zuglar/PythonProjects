# OpenCV2 képbeolvasás, megjelenítés és tükrözés
# OpenCV online dokumentáció: https://docs.opencv.org/


# 3. feladat: Bővítsük a 2. feladatban elkészített programunkat kép transzponálással (sorok és oszlopok cseréje)!
#
#     Használjuk a cv2.transpose() függvényt! A transzponálás a T billentyű lenyomására hajtódjon végre az éppen aktuális képmátrixon!
#     Az angol nyelvű dokumentációban keressünk rá a függvényre, hogy mi a paraméterezése! (Súgó: Egyedül a transzponálandó képet kell paraméterként átadnunk, eredményként a módosítottat kapjuk vissza.)

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

while True:
    key = cv2.waitKeyEx(100)
    if key == 104:
        img = cv2.flip(img, 0)

    if key == 118:
        img = cv2.flip(img, 1)

    if key == 116:
        img = cv2.transpose(img)

    if key == 27 or key == 113:
        break

    cv2.imshow('image', img)

    # print('Lenyomott billentyű és kódja:', key)
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
