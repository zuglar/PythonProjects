# Rajzoljunk pálcikaemberkét és írjuk ki szövegként a nevét!
import numpy as np
import cv2

# 400x200x3 méretű Numpy tömb létrehozása RGB színes képnek
img = np.ndarray((400, 200,3), np.uint8)
# Feltöltés 255 (fehér) színnel
img.fill(255)

legs = np.array([[50, 300], [100, 250], [150, 300]])
arms = np.array([[50, 200], [100, 150], [150, 200]])
cv2.polylines(img, [legs], isClosed=False, color=(192, 0, 0), thickness=5)
cv2.polylines(img, [arms], isClosed=False, color=(192, 0, 0), thickness=5)
cv2.line(img, (100, 130), (100, 250), color=(192, 0, 0), thickness=5)
cv2.circle(img, (100, 110), 20, (192, 0, 0), 5)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'zox1', (75, 350), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

cv2.imshow("image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()