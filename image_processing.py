import cv2
from time import time
import numpy as np


def spinner_detect(img, low_sat=190, high_sat=220, display=False):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    sat = hsv[:, :, 1]
    sat = cv2.medianBlur(sat, 5)
    # mask saturation => every pixel between 180 and 220

    mask = cv2.bitwise_and(cv2.threshold(sat, low_sat, 255, cv2.THRESH_BINARY)[1],
                           cv2.threshold(sat, high_sat, 255, cv2.THRESH_BINARY_INV)[1])

    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, param1=150, param2=50, minDist=30)

    if display:
        if circles is not None:  # code stolen from here : https://www.pyimagesearch.com/2014/07/21/detecting-circles-images-using-opencv-hough-circles/
            # convert the (x, y) coordinates and radius of the circles to integers
            circles = np.round(circles[0, :]).astype("int")
            # loop over the (x, y) coordinates and radius of the circles
            for (x, y, r) in circles:
                # draw the circle in the output image, then draw a rectangle
                # corresponding to the center of the circle
                cv2.circle(img, (x, y), r, (0, 255, 0), 4)
                cv2.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

    print(circles)

    return circles


if __name__ == "__main__":
    img1 = cv2.imread('img1.png')
    t0 = time()
    print(spinner_detect(img1))
    print(time() - t0)
