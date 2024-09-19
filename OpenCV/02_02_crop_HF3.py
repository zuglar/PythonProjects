# Téglalap alakú interaktív területkijelölés
# Készítsünk olyan programot, amely két bal egérgomb kattintással
# (első kattintás: első sarok, második kattintás: átellenes sarok, harmadik kattintás: előző törlése, új kijelölés első sarokpontja, stb.)
# egy téglalapot határoz meg a képen, kivágja a képtartalmat, és új ablakban megjeleníti!
# Az eredeti képre zöld színnel rajzoljuk be a kijelölt téglalapot!

import cv2

# mouse click event definition
def mouse_move_event(event, x, y, flags, param):
    # get global variables
    global image
    if event == cv2.EVENT_MOUSEMOVE:
        image_copy = image.copy()
        image_copy[y:y+ 1] = 0
        image_copy[: , x:x + 1] = 0
        cv2.imshow('image', image_copy)

# read image from file
image = cv2.imread('OpenCV-logo.png', cv2.IMREAD_COLOR)
cv2.imshow('image', image)
cv2.setMouseCallback('image', mouse_move_event)

cv2.waitKey(0)
cv2.destroyAllWindows()