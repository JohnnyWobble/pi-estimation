import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import animation
import math
import random

total = 0
yes = 0

num_iters = 1000

count_pi = np.ndarray((1, num_iters))
count_frame = np.ndarray((1, num_iters))

side = 1.


def pythag(x: float, y: float) -> float:
    """
    Solves the pythagorean theorem for side C

    :param x: x value
    :type x: float
    :param y: y value
    :type y: float
    :return: "side C"
    :rtype: float
    """
    return math.sqrt(x**2 + y**2), x, y


def evaluate() -> (bool, float, float):
    """
    Decides if the points are within 1 unit from (0, 0), and if they are is adds to a counter

    :return: whether (x, y) is within 1 unit of (0, 0); x, y
    :rtype: bool, float, float
    """
    global yes
    global total
    rad, x, y = pythag(random.uniform(-side, side), random.uniform(-side, side))
    if rad <= 1.00000:
        yes += 1
    total += 1
    return rad <= 1.00000, x, y




def difference(frame):
    global yes
    global total
    global count_pi
    global count_frame
    for i in range(10):
        yeah, x, y = evaluate()
        if yeah:
            yes += 1
        total +=1
    count_pi[0][frame] = ((2 * side)**2) * (yes / total)
    count_frame[0][frame] = (10 * (frame + 1))


def animate2(*args):
    difference(args[0])
    print(args[0])
    # print(args)

    arr = np.ndarray([1, len(count_frame)])
    arr.fill(math.pi)
    plt.plot(count_frame, arr[0], 'g')
    return plt.plot(count_frame, count_pi, 'b')





def colordef() -> (str, float, float):
    """
    Decide the color of the point, green if it is within the unit circle, red if not

    :return: color, x, y
    :rtype: str, float, float
    """
    green_bool, x, y = evaluate()
    if green_bool:
        color = 'g'
    else:
        color = 'r'
    return color, x, y


def fix(num) -> str:
    """
    Adds 0s until the number is 8 chars long

    :param num: number to add 0s
    :type num: double
    :return: number with extra 0s
    :rtype: str
    """
    new_num = str(num)
    while len(new_num) < 8:
        new_num += '0'
    return new_num


def animate(*args) -> plt.scatter:
    """
    Is one step in the animation, it adds one dot and changes the title

    :param args: matplotlib can pass stuff in
    :type args: tuple
    :return: the graph
    :rtype: plt.scatter
    """
    print(args)
    color, x, y = colordef()
    plt.title(f"pi = {fix(round((2 * side)**2 * (yes/total), 6))}")
    return plt.scatter(x, y, s=15, c=color, alpha=1)


# def init2


def init(*args) -> plt.scatter:
    """
    This is the first method called, it creates and fills in the graph and then it set the graph to
    have equal scaling on the x and y axis

    :param args: matplotlib can pass stuff in
    :type args: tuple
    :return: the initial graph
    :rtype: plt.scatter
    """
    x_list = np.linspace(-1, 1, 100)
    y_list, y2_list = np.zeros(100), np.zeros(100)
    for num, val in enumerate(x_list):
        y_list[num], y2_list[num] = circle(val)
    plt.axis('equal')
    # plt.scatter(0, 0, 40000, 'g', alpha=.2)
    plt.fill(x_list, y_list, 'g', alpha=.2)
    plt.fill(x_list, y2_list, 'g', alpha=.2)
    return plt.plot(x_list, y_list, 'g', x_list, y2_list, 'g')


def circle(x: float) -> (float, float):
    """
    returns the two y values for an x value in a circle with a radius of 1

    :param x: x value
    :type x: float
    :return: the y values for x
    :rtype: float, float
    """
    y = math.sqrt(1 - (x)**2)
    return y, -y


# for i in range(num_iters):
#     animate2(i)
#
# print(count_pi[0][-1])

# quit()
if __name__ == "__main__":

    # Creates the writer
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=60, metadata=dict(artist='Me'), bitrate=1800)

    # Makes the figure
    fig, _ = plt.subplots()

    # This animates by calling `animate()` 1000 times
    ani = FuncAnimation(fig, animate2, frames=num_iters, repeat=False, interval=.01)#, init_func=init)

    plt.show()  # comment out to hide the animation as its being created
    # ani.save('over_time.mp4', writer)  # <--- uncomment to save the animation



