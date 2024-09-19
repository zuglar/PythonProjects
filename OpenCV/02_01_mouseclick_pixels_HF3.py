# A bal egérgomb kattintási helyének sorában az összes képpont értékét módosítsuk!
# Kérjük le a képmátrix oszlopainak számát a shape attribútummal. Az attribútum értékét tömbként indexelhetjük.
# Ennek második értéke (1-es index!) adja az oszlopok számát. Használjunk for ciklust az értékek módosításához!

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

        # Ha 3 csatárnos a kép
        # if image.ndim == 3:
        #     print('Red: ', image[y, x, 2])
        #     print('Green: ', image[y, x, 1])
        #     print('Blue: ', image[y, x, 0])
        #     image[start_y, start_x] = [0, 0, 255]
        # else:
        #     image[start_y,start_x] = 255 - image[y, x]

        start_x = start_y = -1
        cv2.imshow('image', image)

image = cv2.imread('OpenCV-logo.png', cv2.IMREAD_COLOR)
# image = cv2.imread('OpenCV-logo.png', cv2.IMREAD_GRAYSCALE)
print('Kép indexelhető dimenziói: ', image.ndim)

print('Kép mérete: ', image.shape)
print('Kép pixeltipusa: ', image.dtype)

cv2.imshow('image', image)

# Egérkezelő callback függvény beállitása az ablakhoz
cv2.setMouseCallback('image', mouse_click)

# Kilépés billentyűzetnyomásra
cv2.waitKey(0)
cv2.destroyAllWindows()