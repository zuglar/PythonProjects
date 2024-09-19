# Vonalrajzolás a for ciklus kiváltásával
# Az előző alfejezet példáját (02_01_mouseclick_pixels_HF3.py) módosítsuk úgy, hogy a kattintás helyének sorában ne for ciklussal,
# hanem mátrix szeleteléssel módosítsuk a színértékeket!
# Rajzoljunk függőleges vonalat is!

import cv2

# mouse click event definition
def mouse_click_event(event, x, y, flags, param):
    # get global variables
    global image
    if event == cv2.EVENT_LBUTTONDOWN:
        image_copy = image.copy()
        image_copy[y:y+ 1] = 0
        image_copy[: , x:x + 1] = 0
        cv2.imshow('image', image_copy)

# read image from file
image = cv2.imread('OpenCV-logo.png', cv2.IMREAD_COLOR)
cv2.imshow('image', image)
cv2.setMouseCallback('image', mouse_click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()