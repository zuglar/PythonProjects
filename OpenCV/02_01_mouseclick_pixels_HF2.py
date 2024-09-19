# Próbáljunk más egér eseményre reagálni!
# Nézzük meg mi történik, ha a bal egérgomb lenyomása helyett az egér mozgás (cv2.EVENT_MOUSEMOVE) okoz változást!

import cv2

# x és y koordináták alapbeállitása
start_x = start_y = -1

def mouse_move(event, x, y, flags, param):
    # Globális változó átvétele
    global image, start_x, start_y

    start_x = x
    start_y = y

    print('start_x: ', start_x)
    print('start_y: ', start_y)

    # if event == cv2.EVENT_LBUTTONDOWN:
    #     # (x, y) szinérték kiirás
    #     print('Pixel: ', image[y, x])
    #
    #     # Ha 3 csatárnos a kép
    #     if image.ndim == 3:
    #         print('Red: ', image[y, x, 2])
    #         print('Green: ', image[y, x, 1])
    #         print('Blue: ', image[y, x, 0])
    cv2.imshow('image', image)

image = cv2.imread('OpenCV-logo.png', cv2.IMREAD_COLOR)
# image = cv2.imread('OpenCV-logo.png', cv2.IMREAD_GRAYSCALE)
print('Kép indexelhető dimenziói: ', image.ndim)
print('Kép mérete: ', image.shape)
print('Kép pixeltipusa: ', image.dtype)

cv2.imshow('image', image)

# Egérkezelő callback függvény beállitása az ablakhoz
cv2.setMouseCallback('image', mouse_move)

# Kilépés billentyűzetnyomásra
cv2.waitKey(0)
cv2.destroyAllWindows()