"""
File: 
Name: Sabrina Wang
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
ball.color = 'black'
ball.filled = True
ball.fill_color = 'black'
num_click = 1   # controls within 3 round of bounces
button = 0    # helps the ball will be not affected by the click during each bounce


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(ball, START_X, START_Y)
    onmouseclicked(bouncing_ball)


def bouncing_ball(mouse):
    global num_click, button
    button += 1  # if the user clicks once at the beginning, adds 1 to the button, means start bouncing
    if button == 1:
        if num_click < 4:  # if the round is within 3 round
            vy = 0
            while True:
                ball.move(VX, vy+GRAVITY)
                vy = vy+GRAVITY
                if ball.y+SIZE >= window.height:
                    vy = -vy
                    ball.move(VX, vy*0.9)
                    vy = vy*0.9
                pause(DELAY)
                if ball.x+SIZE >= window.width:  # if the ball jumps over the window
                    window.remove(ball)
                    break
            num_click += 1
        else:
            window.add(ball, START_X, START_Y)
        button = 0


if __name__ == "__main__":
    main()
