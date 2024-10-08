# Szálkereszt rajzolás
# Rajzoljunk célkeresztet az egér ablakterületen való követéséhez! Színes kép esetén a vonal színe legyen sárga, szürkeárnyalatos kép esetén 192 intenzitású szürke!
# Ötlet: Mentsük el a bementi kép másolatát, és minden újrarajzoláskor annak másolatára rajzoljunk!

import cv2

def mouse_event(event, x, y, flags, param):
    global height, width, image
    if event == cv2.EVENT_MOUSEMOVE:
        print('Pixel: ', y, x)
        # cv2.line(img, (100, 130), (100, 250), color=(192, 0, 0), thickness=5)
        image_copy = image.copy()
        if color_mode:
            cv2.line(image_copy, (0, y), (width, y), color=(0, 255, 255), thickness=1)
            cv2.line(image_copy, (x, 0), (x, height), color=(0, 255, 155), thickness=1)
        else:
            cv2.line(image_copy, (0, y), (width, y), color=(192, 192, 192), thickness=1)
            cv2.line(image_copy, (x, 0), (x, height), color=(192, 0, 0), thickness=1)

        cv2.imshow('image', image_copy)

open_mode = input('Open file in:\n'
             'Press \'c\' - color mode\n'
             'Press \'k\' - black & white mode\n')
image = None
color_mode = True
height = width = color = 0
if open_mode == 'c':
    print('c')
    image = cv2.imread('../OpenCV-logo.png')
    height, width, color = image.shape
elif open_mode == 'k':
    print('k')
    color_mode = False
    image = cv2.imread('../OpenCV-logo.png', cv2.IMREAD_GRAYSCALE)
    height, width = image.shape
else:
    exit(0)
cv2.imshow('image', image)

cv2.setMouseCallback('image', mouse_event)

cv2.waitKey(0)
exit(0)