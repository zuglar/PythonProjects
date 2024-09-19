# OpenCV2 képbeolvasás, megjelenítés és tükrözés
# OpenCV online dokumentáció: https://docs.opencv.org/

# 4. feladat: Kép forgatása balra és jobbra 90 fokkal
#
# Gyakori probléma, hogy a kép készítésekor a kamera állása nem megfelelő, így 90 fokkal elforgatott képet kapunk. Bővítsük az előző programunkat úgy, hogy korrigálni tudjuk ezt!
#
#     A cv2.flip() és a cv2.transpose() függvények megfelelő kombinációjával biztosítsunk lehetőséget a képmátrix 90 fokkal való balra és jobbra forgatására!
#     Az R és L billentyűkkel érhessük el ezeket a funkciókat. A műveletek az éppen aktuális képmátrixra vonatkozzanak!
#     A 3. feladat programjával tapasztaljuk ki, milyen sorrendben kell az egyes műveleketet elvégeznünk a megfelelő forgatásokhoz.
#     A megoldáshoz a cv2.rotate() is használható. Keressük meg a dokumentációban a használatát!

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
    if key == 108:
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    if key == 114:
        img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

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
