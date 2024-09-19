# Oldjuk meg, hogy az egér mozgására reagálva mindig az aktuális pozícióhoz rajzolódjon vízszintes és függőleges vonal! (Szálkereszt rajzolás.)
# Ne felejtsük el az eredeti képet eltárolni, és minden új rajzolás előtt visszamásolni.

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