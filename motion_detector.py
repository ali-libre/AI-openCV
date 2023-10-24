# !/bin/python3
import cv2
# import time
# import numpy as np
cap = cv2.VideoCapture("motion720.mp4")

ret1, frame1 = cap.read()
ret2, frame2 = cap.read()

while True:

    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame1_grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame2_grey = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    frame1_blur = cv2.GaussianBlur(frame1_grey, (21, 21), 1)
    frame2_blur = cv2.GaussianBlur(frame2_grey, (21, 21), 1)


    diff = cv2.absdiff(frame1_blur, frame2_blur)
    thresh = cv2.threshold(diff, 20, 255, cv2.THRESH_BINARY)[1]
    print(diff)
    final = cv2.dilate(thresh, None, iterations=25)
    cv2.imshow("Demo", frame1)
    cv2.imshow("diff", diff)
    cv2.imshow("Motion", final)


    frame1 = frame2
    ret, frame2 = cap.read()

    if not ret:
        break


    k = cv2.waitKey(10)
    if k == ord('p'):
        while True:
            # time.sleep(50)
            k = cv2.waitKey(10)
            if k == ord('p'):
                break

    if k == ord('q'):
        break

cv2.destroyAllWindows()
