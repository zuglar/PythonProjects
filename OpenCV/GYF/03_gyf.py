'''Készítsünk egyszerű rajzolóprogramot!

    A program indításakor hozzunk létre egy 480 sorból és 640 oszlopból álló BGR színes képmátrixot, np.uint8 típussal.
    A képet töltsük fel fehér színnel ([255, 255, 255] BGR érték) és jelenítsük meg.
    A program kezelje az egéreseményeket az OpenCV lehetőségeit használva.
    Egy globális változóban tároljuk, hogy a bal egérgomb lenyomásra vagy felengedésre került legutóbb. A program indulásakor feltételezzük, hogy nincs lenyomva.
    Az egér mozgás eseménykor, amennyiben az egér bal gombja lenyomott állapotban van (az előző pontban tárgyalt globális változó lenyomott állapotot jelez),
    akkor az egér pozícióba rajzoljunk ki egy adott sugarú és színű, kitöltött kört. (Ne felejtsük el újra megjeleníteni a képet a rajzolás után!)
    A kör aktuális sugarát szintén globális változóban tároljuk, alapértéke legyen 10. A színt szintén, az legyen vörös [0, 0, 255].
    A + és a - billentyűk lenyomására növeljük, illetve csökkentsük a rajzolandó kör sugarát 5 egységgel! A sugár értéke maradjon az [5, 100] tartományban.
    Az r, g, b, k, w billentyűk lenyomásával állítsuk a rajzolószínt vörösre ([0, 0, 255]), zöldre ([0, 255, 0]), kékre ([255, 0, 0]), feketére ([0, 0, 0]),
    illetve fehérre ([255, 255, 255]).
    A t billentyű lenyomására töltsük fel a teljes képet fehér színnel (törlés).
    Az s billentyű lenyomására rögzített nevű fájlba mentsük el az aktuális képmátrixot, PNG formátumban.
    A q vagy az ESC billentyű lenyomásával léphessünk ki a programból.

Készítsünk saját rajzot a programmal és mentsük el PNG fájlba!

A rajzolóprogram bővítése
Az előző rajzolóprogramunk működik, de használata nem kényelmes. Nem látjuk, hogy a bal egérgomb lenyomásával milyen színű és
méretű elem rajzolódik ki. Bővítsük úgy a programot, hogy az egér mozgatásakot lássuk, milyen elem jelenne meg!

Ötlet: Legyen két képmátrixunk. Egy, amely az érvényes rajzolásokat tartalmazza, és egy másik, amire pluszban ideiglenesen rárajzoljuk azt az elemet is,
ami kattintással megjelenne. Arra kell figyelni, hogy egy következő ideiglenes elem rajzolását az érvényes rajzolást tartalmazóra kell elhelyezni.
Megjeleníteni az ideiglenest kell. Figyeljünk arra is, hogy mentéskor melyik képmátrixot használjuk!


További lehetséges rajzolási funkciók
A rajzolóprogramunkat további funkciókkal bővthetjük. Néhány ötlet:

    Ne üres fehér képből induljunk, hanem fájlból töltsünk be egyet. A t billentyűvel ekkor az eredeti képet állítsuk vissza.
    Rajzolásra választhassunk más geometriát is a kör helyett.

'''
import math

import cv2
import numpy as np

mouse_left_btn_press = False
mouse_left_btn_release = True
size = 10
color = (0, 0, 255)
geometry = 0
start_x = start_y = -1
x1 = x2 = x3 = y1 = y2 = y3 = 0

# mouse events
def mouse_events(event, x, y, flags, param):
    global image, mouse_left_btn_press, mouse_left_btn_release
    global size, color, start_x, start_y

    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_left_btn_press = True
        mouse_left_btn_release = False
        print('Pixel: ', y, x)

        center_calculate(x, y)
        draw(x, y)

    if event == cv2.EVENT_LBUTTONUP:
        mouse_left_btn_press = False
        mouse_left_btn_release = True

    if event == cv2.EVENT_MOUSEMOVE:
        if mouse_left_btn_press:
            print('Pixel: ', y, x)

            center_calculate(x, y)
            draw(x, y)

# # 480 * 640 méretű Numpy tömb létrehozása RGB színes képnek
# image = np.ndarray((480, 640, 3), np.uint8)
# # Feltöltés fehér színnel ([255, 255, 255] BGR érték)
# image[:] = (255, 255, 255)


def center_calculate(x, y):
    global geometry, x1, x2, x3, y1, y2, y3, size
    print('Center calculate')
    if geometry == 0:
        x1 = x
        y1 = y

    if geometry == 1:
        x1 = int(x - size / 2)
        y1 = int(y - size / 2)
        x2 = int(x + size / 2)
        y2 = int(y + size / 2)

    if geometry == 2:
        base = int(size * math.sqrt(3) / 2 / 2)
        x1 = int(x - base)
        y1 = int(y + base)
        x2 = int(x + base)
        y2 = int(y + base)
        x3 = int(x)
        y3 = int(y - base)

def draw(x, y):
    print('draw')
    global image, geometry, x1, x2, x3, y1, y2, y3, size, color

    if geometry == 0:
        cv2.circle(image, (x1, y1), size, color, -1)

    if geometry == 1:
        cv2.rectangle(image, (x1, y1), (x2, y2), color, -1)

    if geometry == 2:
        polygon1 = np.array([[x1, y1], [x2, y2], [x3, y3]])
        cv2.fillPoly(image, [polygon1], color)

    cv2.imshow('image', image)

def change_tool():
    print('change tool')
    global tool_image, size, color, start_x, start_y, geometry
    global x1, x2, x3, y1, y2, y3
    #center_x = center_y = 105
    print('geometry: ', geometry)

    if color == (255, 255, 255):
        tool_image[:] = (0, 0, 0)
    else:
        tool_image[:] = (255, 255, 255)

    center_calculate(105, 105)

    if geometry == 0:
        cv2.circle(tool_image, (x1, y1), size, color, -1)

    if geometry == 1:
        cv2.rectangle(tool_image, (x1, y1), (x2, y2), color, -1)

    if geometry == 2:
        # polygon
        polygon1 = np.array([[x1, y1], [x2, y2], [x3, y3]])
        cv2.fillPoly(tool_image, [polygon1], color)

    cv2.imshow('tool_image', tool_image)

# image read from file
image = cv2.imread('../GolyoAlszik_rs.jpg')
# create tool window
tool_image = np.ndarray((210, 210, 3), np.uint8)
tool_image[:] = (255, 255, 255)

cv2.circle(tool_image, (105, 105), size, color, -1)

# Kép megjelenítése ablakban
cv2.imshow('image', image)

cv2.imshow('tool_image', tool_image)

cv2.setMouseCallback('image', mouse_events)

while True:
    key = cv2.waitKeyEx(0)
    # print('key: ', key)
    # key + : 43
    if key == 43:
        print('key +')
        if size < 100:
            size += 5
            print('size: ', size)
            change_tool()
    # key - : 45
    if key == 45:
        print('key -')
        if size > 5:
            size -= 5
            print('size: ', size)
            change_tool()
    # key r : 114
    if key == 114:
        print('key r - red')
        color = (0, 0, 255)
        change_tool()
    # key g : 103
    if key == 103:
        print('key g -  green')
        color = (0, 255, 0)
        change_tool()
    # key b : 98
    if key == 98:
        print('key b - blue')
        color = (255, 0, 0)
        change_tool()
    # key k : 107
    if key == 107:
        print('key k - black')
        color = (0, 0, 0)
        change_tool()
    # key w : 119
    if key == 119:
        print('key w - white')
        color = (255, 255, 255)
        change_tool()
    # key t : 116
    if key == 116:
        print('key t - delete')
        # image[:] = [255, 255, 255]
        image = cv2.imread('GolyoAlszik_rs.jpg')
    # key s : 115
    if key == 115:
        print('key s - save')
        cv2.imwrite('My_image.png', image)
    # key x : 12
    if key == 120:
        print('key x - change geometry')
        geometry += 1
        if geometry == 3:
            geometry = 0

        change_tool()

    cv2.imshow('image', image)

    # key q : 113, key esc : 27
    if key == 27 or key == 113:
        print('Exit')
        break

# Összes ablak bezárása
cv2.destroyAllWindows()
