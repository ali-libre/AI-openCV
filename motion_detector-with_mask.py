# !/bin/python3

import cv2
import numpy as np


cap = cv2.VideoCapture("rtsp://admin:qwert12345@192.168.43.190:10233/h264_ulaw.sdp")
# camera = cv2.VideoCapture("rtsp://admin:<port>@<ip>/xyz/video.smp")


ret1, frame1 = cap.read()
ret2, frame2 = cap.read()


def waitToKey():
    return cv2.waitKey(5)


def waitToPause(key):
    if key == ord('p'):
        while True:
            key = cv2.waitKey(10)
            if key == ord('p'):
                break


def waitToQuit(key):
    if key == ord('q'):
        return True


while True:
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame1_grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame2_grey = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    frame1_blur = cv2.GaussianBlur(frame1_grey, (21, 21), 1)
    frame2_blur = cv2.GaussianBlur(frame2_grey, (21, 21), 1)

    diff = cv2.absdiff(frame1_blur, frame2_blur)
    thresh = cv2.threshold(diff, 20, 255, cv2.THRESH_BINARY)[1]
    # print(diff)
    final = cv2.dilate(thresh, None, iterations=15)
    masked = cv2.bitwise_and(frame1, frame1, mask=final)
    white_pixel = np.sum(thresh) / 255
    row, col = thresh.shape
    total = row * col
    # print(total * .01)
    if white_pixel:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame1, "Movement Detected", (10, 50), font, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.namedWindow('masked', flags=cv2.WINDOW_GUI_NORMAL)
    cv2.namedWindow('final', flags=cv2.WINDOW_GUI_NORMAL)
    cv2.namedWindow('Demo', flags=cv2.WINDOW_GUI_NORMAL)
    cv2.namedWindow('diff', flags=cv2.WINDOW_GUI_NORMAL)
    cv2.namedWindow('Motion', flags=cv2.WINDOW_GUI_NORMAL)
    # cv2.namedWindow('masked',cv2.WND_PROP_FULLSCREEN)
    # cv2.setWindowProperty("masked", CV_WND_PROP_FULLSCREEN, CV_WINDOW_FULLSCREEN);
    cv2.imshow("Demo", frame1)
    cv2.imshow("diff", diff)
    cv2.imshow("Motion", thresh)
    cv2.imshow("final", final)
    cv2.imshow("masked", masked)

    frame1 = frame2
    ret, frame2 = cap.read()

    key = waitToKey()
    waitToPause(key)
    if waitToQuit(key):
        break

    if not ret:
        break


cv2.destroyAllWindows()
