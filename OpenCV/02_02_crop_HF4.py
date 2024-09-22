# Színértékek módosítása egy területen belül
# Színes kép esetén egy megadott téglalap alakú képtartományban a vörös csatorna értékeit állítsuk 192-re!
# Utána a másik két csatorna értékét nullázzuk ki ugyanezen a területen!

import cv2

num_click = 0
start_x = start_y = end_x = end_y = -1
# mouse click event definition
def mouse_left_click(event, x, y, flags, param):
    # get global variables
    global image, num_click, start_x,start_y, end_x, end_y
    if event == cv2.EVENT_LBUTTONDOWN:
        num_click += 1
        if num_click == 1:
            start_x = x
            start_y = y
        elif num_click == 2:
            if y <= start_y:
                end_y = start_y
                start_y = y
            else:
                end_y = y

            if x <= start_x:
                end_x = start_x
                start_x = x
            else:
                end_x = x
            print('sx: ', start_x, 'sy: ', start_y, ' - ex: ', end_x, ' ey: ', end_y)
            image[start_y:end_y, start_x:end_x] = [0, 0, 192]
            cv2.imshow('image', image)
            num_click = 0
        else:
            num_click = 0


# read image from file
image = cv2.imread('GolyoAlszik_rs.jpg', cv2.IMREAD_COLOR)
cv2.imshow('image', image)
cv2.setMouseCallback('image', mouse_left_click)

cv2.waitKey(0)
cv2.destroyAllWindows()