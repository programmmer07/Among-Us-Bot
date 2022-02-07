import cv2
import numpy as np
from matplotlib import pyplot as plt
import pyautogui as pag
from time import sleep as sp


while True:
    # Convert image to grayscale
    im = pag.screenshot('foo.jpg') # im = pag.screenshot('foo.jpg', region=(0,0, 300, 400))


    img_gs = cv2.imread('foo.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imwrite('gs.jpg', img_gs)

    # Declaring the output graph's size
    plt.figure(figsize=(16, 16))
    # Apply canny edge detector algorithm on the image to find edges
    edges = cv2.Canny(img_gs, 150, 250)

    # returns a Pillow/PIL Image object
    cv2.imwrite('edge.jpg', edges)

    # Display the two images
    plt.subplot(121), plt.imshow(img_gs)
    plt.title('Original Gray Scale Image')

    plt.subplot(122), plt.imshow(edges)
    plt.title('Edge Image') # Plot the original image against the edges
    plt.show()
    plt.pause(0.0001)
    # plt.clf()
    sp(.7)
    plt.close()