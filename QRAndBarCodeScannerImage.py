import cv2
import numpy as np
from pyzbar import pyzbar

img = cv2.imread('qrcode.jpg')
codes = pyzbar.decode(img)

code = codes[0]

data = code.data.decode('utf-8')

x, y, w, h = code.rect

polygon = code.polygon

points = np.array([polygon], np.int32)
points = points.reshape((-1, 1, 2))
img = cv2.polylines(img, [points], True, (0, 255, 0), 6)

img = cv2.putText(img, data, (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
