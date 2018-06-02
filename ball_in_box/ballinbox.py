import math
import random
from .validate import validate

__all__ = ['ball_in_box']


def ball_in_box(m=5, blockers=[(0.5, 0.5), (0.5, -0.5), (0.5, 0.3)]):
    """
    m is the number circles.
    n is the list of coordinates of tiny blocks.
    This returns a list of tuple, composed of x,y of the circle and r of the circle.
    """

    # The following is an example implementation.

    return find_radius(blockers, m)


def find_radius(blockers, m):
    circles = []
    # 每个格子的坐标
    test_x = []
    test_y = []
    # 当前放入的圆环数量
    circle_index = 0

    inc = 7e-3
    times = (int)(2 / inc)
    begin = -1 + inc

    for i in range(times):
        test_x.append(begin)
        test_y.append(begin)
        begin += inc

    for i in range(m):

        tmp_y = -1 + inc
        x = tmp_y
        y = tmp_y
        r = inc

        # 第一次遍历
        for tmp_y in test_y:
            for tmp_x in test_x:
                tmp_r = min_radius(tmp_x, tmp_y, circles, blockers)
                if r < tmp_r:
                    x = tmp_x
                    y = tmp_y
                    r = tmp_r

        # 第二次遍历
        tmp_x = x - inc
        tmp_inc = inc / 20
        for i in range(20):
            tmp_x += tmp_inc
            tmp_y = y - inc
            for j in range(20):
                tmp_y += tmp_inc
                tmp_r = min_radius(tmp_x, tmp_y, circles, blockers)
                if r < tmp_r:
                    x = tmp_x
                    y = tmp_y
                    r = tmp_r

        circles.append((x, y, r))
        print(x, y, r)
        circle_index += 1

    return circles


# 找出满足条件的最大圆的半径
def min_radius(x, y, circles, blockers):
    if (1 - abs(x)) > (1 - abs(y)):
        r = (1 - abs(y))
    else:
        r = (1 - abs(x))

    for blocker in blockers:
        tmp = math.sqrt((blocker[0] - x) ** 2 + (blocker[1] - y) ** 2)

        if (r > tmp):
            r = tmp

    for circle in circles:
        tmp = math.sqrt((circle[0] - x) ** 2 + (circle[1] - y) ** 2) - circle[2]

        if (r > tmp):
            r = tmp

    return r
