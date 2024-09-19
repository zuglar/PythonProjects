# A bal egérgomb kattintási helyének sorában az összes képpont értékét módosítsuk!
# Kérjük le a képmátrix oszlopainak számát a shape attribútummal. Az attribútum értékét tömbként indexelhetjük.
# Ennek második értéke (1-es index!) adja az oszlopok számát. Használjunk for ciklust az értékek módosításához!

# Egészítsük ki a programot billentyűzet kezeléssel!
#
# Az r billentyű lenyomására állítsuk vissza az eredeti képet! A q billentyű lenyomására lépjünk ki a programból.
# Minden más billentyű lenyomására ne történjen semmi érdemleges, folytatódjon a billentyűkezelő ciklus.

import cv2

# x és y koordináták alapbeállitása
start_x = start_y = -1
def mouse_click(event, x, y, flags, param):
    # Globális változó átvétele
    global image, start_x, start_y

    if event == cv2.EVENT_LBUTTONDOWN:
        # (x, y) szinérték kiirás
        # print('Pixel: ', image[y, x])
        start_x = x
        start_y = y

        print('start_x: ', start_x)
        # print('start_y: ', start_y)
        [x1, y1, z1] = image.shape
        print('x1: ', x1)
        print('y1: ', y1)
        for i in range(0, y1):
            image[start_y, i] = [0, 0, 0]

        start_x = start_y = -1
        cv2.imshow('image', image)



image = cv2.imread('OpenCV-logo.png', cv2.IMREAD_COLOR)

image_copy = image.copy()
# image = cv2.imread('OpenCV-logo.png', cv2.IMREAD_GRAYSCALE)
print('Kép indexelhető dimenziói: ', image.ndim)

print('Kép mérete: ', image.shape)
print('Kép pixeltipusa: ', image.dtype)

cv2.imshow('image', image)


# Egérkezelő callback függvény beállitása az ablakhoz
cv2.setMouseCallback('image', mouse_click)


while True:
    key = cv2.waitKeyEx(100)
    if key == 114: # 'r' key
        image = image_copy.copy()
        cv2.imshow('image', image_copy)

    if key == 113: # 'q' keyq
        break

cv2.destroyAllWindows()