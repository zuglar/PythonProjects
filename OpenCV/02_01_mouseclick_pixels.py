import cv2

def mouse_click(event, x, y, flags, param):
    # Globális változó átvétele
    global image

    if event == cv2.EVENT_LBUTTONDOWN:
        # (x, y) szinérték kiirás
        print('Pixel: ', image[y, x])

        # Ha 3 csatárnos a kép
        if image.ndim == 3:
            print('Red: ', image[y, x, 2])
            print('Green: ', image[y, x, 1])
            print('Blue: ', image[y, x, 0])
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