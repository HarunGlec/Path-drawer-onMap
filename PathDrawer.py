import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('map.png',0)
img = cv2.medianBlur(img,5)
ret,th1 = cv2.threshold(img,240,255,cv2.THRESH_BINARY_INV)
cv2.imwrite('paths.png',th1)

#You can also try Adaptive mean and adaptive gaussian algorithm 
#th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
#th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

plt.imshow(th1,'gray')
plt.title('Paths on Map')
plt.show()
