import cv2
from sympy import is_amicable

image = cv2.imread('GolyoAlszik_rs.jpg')

# Képkivágás; sor és oszlop tartomány megadása
cropped = image[82:172, 396:486]

# Képkivágás; sor és oszlop tartomány megadása
image[10:100, 20:110] = cropped

image[200:, :] = [0, 255, 255]

image[:, 300:, 2] = 0

image[:, 30:50] = 255
image[100:120] = 255

print('image.shape', image.shape[1])
image[:, (image.shape[1] >> 1) - 50:(image.shape[1] >> 1) + 50] = 128

cv2.imshow('image', image)
cv2.imshow('cropped', cropped)
cv2.waitKey(0)

cv2.destroyAllWindows()

image[200:, :] = [0, 255, 255]