#!/bin/python3
import cv2
import numpy as np
import math


def cature_histogram(source):
    cap = cv2.VideoCapture(source)
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (1000, 600))
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, 'Plcae region of hand inside box & press `a`',
                    (50, 50), font, .7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.rectangle(frame, (500, 100), (580, 100), (105, 105, 105), 2)
        box = frame[105:175, 505:575]

        cv2,imshow("capture Histogram", frame)
        key = cv2.waitKey(10)
        if key == 97:
            object_color = box
            cv2.destroyAllWindows()
            break
        if key == ord('q'):
            cv2.destroyAllWindows
            cap.release
            break
        object_color_hsv = cv2.cvtColor(object_color, cv2.COLOR_BGR2HSV)
        object_hist = cv2.calcHist([object_color_hsv], [0, 1], None,
                                   [12,15], [0, 180, 0, 256])

        cv2.normalize(object_hist, object_hist, 0, 255, cv2.NORM_MINMAX)
        return object_hist


cap = cv2.VideoCapture("rtsp://admin:qwert12345@192.168.43.190:10233/h264_ulaw.sdp")

while True:
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
    ret, frame = cap.read()
    if not ret:
        break
    cv2.namedWindow("test", flags=cv2.WINDOW_GUI_NORMAL)
    cv2.imshow("test", frame)


cap.release()
cv2.destroyAllWindows()
