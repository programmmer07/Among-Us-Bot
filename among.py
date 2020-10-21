import pyautogui as pag
from time import sleep as sp
import im
import cv2
import numpy as np
from random import choice as ch
import cont

pag.FAILSAFE = False
def dis_to_vector(image, pos, dx, dy):
    x = 0
    y = 0
    try:
        while np.all(image[pos[0]+x, pos[1]+y] == [0, 0, 0]):
            x += dx
        y += dy
        return [abs(x), abs(y)]
    except:
        return [0, 0]
# preparation 
WIDTH, HEIGHT = pag.size() # Get the size of the primary monitor.
cmds = ['A', 'S', 'D']
index = 0
def add(a, b, arr):
    if len(arr) < 5:
        arr.append(a)
    else:
        arr.pop(0)
        arr.append(a)
    if len(arr) < 5:
        arr.append(b)
    else:
        arr.pop(0)
        arr.append(b)
    return arr

m1 = []
m2 = []
def check_position(v):
    global index
    pag.screenshot("edge/s.png")
    cont.cont(cv2.imread("edge/s.png"), "edge/" + str(index) + ".png")

def press(k):
    pag.keyDown(k)
    sp(.2)
    pag.keyUp(k)

def move_vector(v1, v2):
    c = check_position(v1)
    if c[0] or c[1]:
        press(v2)


print('bot has started, now you have 3 seconds to leave')
sp(3)
print('bot started...')
while True:
    check_position(1)
    image = cv2.imread("edge/" + str(index) + ".png")
    left = dis_to_vector(image, [560, 511], -1, 0)
    right = dis_to_vector(image, [721, 524], 1, 0)
    up = dis_to_vector(image, [630, 403], 0, -1)
    down = dis_to_vector(image, [635, 611], 0, 1)
    