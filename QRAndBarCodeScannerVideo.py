import cv2
from pyzbar import pyzbar
import numpy as np

video = cv2.VideoCapture(0)

while True:
    _, img = video.read()
    codes = pyzbar.decode(img)
    for code in codes:
        data = code.data.decode('utf-8')
        print(data)
        x, y, w, h = code.rect
        polygon = code.polygon
        points = np.array([polygon], np.int32)
        points = points.reshape((-1, 1, 2))
        img = cv2.polylines(img, [points], True, (0, 255, 0), 4)
        img = cv2.putText(img, data, (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
    cv2.imshow('Video', img)
    cv2.waitKey(1)
