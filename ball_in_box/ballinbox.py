# -*- coding: utf-8 -*-
import math
import random
import sys
from ball_in_box import config

__all__ = ['ball_in_box']


def prod_dots(xrange, yrange, percision):
    """
        Divide areas
    """
    dots = []
    interval = (xrange[1] - xrange[0]) * 1.0 / percision
    y_num = int((yrange[1] - yrange[0]) / interval)
    for i in range(1, percision):
        for j in range(1, y_num):
            dots.append((xrange[0] + i * interval, yrange[0] + j * interval))

    return dots


def get_max_r(dot, xrange, yrange, blockers, circles):
    """
        Get the largest radius
    """
    r_list = []
    r_list.append(abs(dot[0] - xrange[0]))
    r_list.append(abs(dot[0] - xrange[1]))
    r_list.append(abs(dot[1] - yrange[0]))
    r_list.append(abs(dot[1] - yrange[1]))
    for blocker in blockers:
        d = math.sqrt((dot[0] - blocker[0])**2 + (dot[1] - blocker[1])**2)
        r_list.append(d)

    for circle in circles:
        d = math.sqrt((dot[0] - circle[0])**2 +
                      (dot[1] - circle[1])**2) - circle[2]
        # if in other circles, skip it
        if d <= 0:
            return 0
        r_list.append(d)

    r = sys.maxsize
    for item in r_list:
        if item < r:
            r = item
    return r

def get_center(num_of_circle,dots):
    return
def get_radius(dots):
    radius=[]
    k=len(dots)
    l=0
    for l in range(k):
        radius[l]=random.random();
    return radius
    for i in range(k):
        j=i+1
        for j in range(k):
            if(((dots[i][0]-dots[j][0])**2 + (dots[i][1]-dots[j][1])**2)<radius[i]+radius[j]):


def ball_in_box(num_of_circle, blockers):
    """
        Main body of algorithm: Greedy Algorithm
    """
    xrange = config.XRANGE
    yrange = config.YRANGE
    percision = config.PERCISION
    circles = []
    dots = prod_dots(xrange, yrange, percision)
    for i in range(num_of_circle):
        temp_r = 0
        circle = [0, 0, 0]
        for dot in dots:
            r = get_max_r(dot, xrange, yrange, blockers, circles)
            if r > temp_r:
                temp_r = r
                circle[0] = dot[0]
                circle[1] = dot[1]
                circle[2] = temp_r

        dots.remove((circle[0], circle[1]))
        circles.append((circle[0], circle[1], circle[2]))

    return circles