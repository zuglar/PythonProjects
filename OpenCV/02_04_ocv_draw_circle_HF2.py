# Rajzoljunk stilizált autót és írjuk ki szövegként a rendszámát!
import numpy as np
import cv2

# 300x400x3 méretű Numpy tömb létrehozása RGB színes képnek
img = np.ndarray((300, 400, 3), np.uint8)
# Feltöltés 255 (fehér) színnel
img.fill(255)


cv2.rectangle(img, (60, 120), (330, 180), (255, 0, 0), 2)
cv2.circle(img, (120, 200), 20, (255, 0, 0), 2)
cv2.circle(img, (270, 200), 20, (255, 0, 0), 2)
cv2.ellipse(img,(200, 120),(90, 70), 0, 180, 360, (255, 0, 0), 2)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'AA IV-679', (140, 280), font, 0.6, (255, 0, 0), 1, cv2.LINE_AA)

cv2.imshow("image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()