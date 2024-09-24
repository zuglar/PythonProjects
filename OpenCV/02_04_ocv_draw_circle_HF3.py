# Rajzoljunk stilizált házat, a homlokzaton házszámmal!

import numpy as np
import cv2

# 250x400x3 méretű Numpy tömb létrehozása RGB színes képnek
img = np.ndarray((250, 400, 3), np.uint8)
# Feltöltés 255 (fehér) színnel
img.fill(255)

cv2.rectangle(img, (50, 140), (150, 240), (0, 255, 0), 2)

contour1 = np.array([[50, 140], [35, 140], [100, 70], [165, 140], [150, 140]])
cv2.polylines(img, [contour1], isClosed=False, color=(0, 255, 0), thickness=2)

contour2 = np.array([[100, 70], [250, 70], [325, 140], [165, 140]])
cv2.polylines(img, [contour2], isClosed=False, color=(0, 255, 0), thickness=2)

contour3 = np.array([[300, 140], [300, 240], [150, 240]])
cv2.polylines(img, [contour3], isClosed=False, color=(0, 255, 0), thickness=2)

font = cv2.FONT_ITALIC
cv2.putText(img, '13', (110, 170), font, 0.8, (0, 0, 0))

cv2.imshow('img', img)

cv2.waitKey(0)

cv2.destroyAllWindows()