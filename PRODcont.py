import cv2
import numpy as np
import pyautogui as pag
# from time import sleep as sp


class ScreenShot:
    """
    Function for our AmongUs bot. Function just makes screenshot and returns it as a contoured image
    """

    @staticmethod
    def pos():
        # sp(3) TEST ONLY

        screen = pag.screenshot('screen.jpg')

        img = cv2.imread('screen.jpg', cv2.IMREAD_UNCHANGED)

        # convert img to grey
        img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # set the thresh
        thresh = 35

        # get threshold image
        ret, thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)

        # find contours
        contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # create an empty image for contors
        img_contours = np.zeros(img.shape)

        # draw the contours on the empty image
        cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 3)

        # save image
        cv2.imwrite('contours.jpg', img_contours)