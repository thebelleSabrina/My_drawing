"""
File: 
Name: Sabrina Wang
-------------------------
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line appears
at the condition where the circle disappears as the user clicks
on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the GOval
SIZE = 10

# global variable
window = GWindow()
click_num = 0  # how many times user click
point1 = GOval(SIZE, SIZE, x=0, y=0)  # the beginning of every line


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(mouse):
    global click_num, point1
    if click_num % 2 == 0:  # first click, click = 0, appears a circle
        point1 = GOval(SIZE, SIZE, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        window.add(point1)
    else:   # second click, click = 1, the circle disappears as a line appears
        line = GLine(point1.x, point1.y, mouse.x, mouse.y)
        window.add(line)
        window.remove(point1)
    click_num += 1


if __name__ == "__main__":
    main()
