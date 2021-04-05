"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

Set up the initial environment and function of breakout game in this file.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random
from campy.gui.events.timer import pause

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BRICK_SECTION = 5      # Number of sections of bricks. (>=0, <=5)
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.__window = GWindow(width=window_width, height=window_height, title=title)

        # Switch controls whether the game starts. If True, start the game.
        self.switch = False

        # Greeting Page involves: bg as background / wd1 as welcome words / wd2 as start bottom
        #                       / button as the background of the start button.
        self.__grt_bg = GRect(self.__window.width, self.__window.height)
        self.__grt_bg.filled = True
        self.__grt_bg.fill_color = 'white'
        self.__grt_bg.color = 'white'

        # grt_wd: Welcome to BREAKOUT GAME.
        self.__grt = GLabel('WELCOME\nTO\nBREAKOUT\nGAME')
        self.__grt_wd1 = GLabel('WELCOME\nTO\nBREAKOUT\nGAME', self.__window.width / 3 -
                                self.__grt.width / 2, self.__window.height / 3)
        font_size = 18 * self.__window.width/445
        self.__grt_wd1.font = 'Courier-18'

        # grt_bottom: black rectangle
        self.__grt_button = GRect(100, 40,
                                  x=self.__window.width / 3 - self.__grt.width / 2,
                                  y=self.__window.height * 2 / 3 - self.__grt.height * 2.5)
        self.__grt_button.filled = True

        # grt_wd: START!
        self.__grt_wd2 = GLabel('START!', self.__window.width / 3 -
                                self.__grt.width / 2, self.__window.height * 2 / 3)
        self.__grt_wd2.font = 'Courier-28'
        self.__grt_wd2.color = 'white'

        # Create a paddle to catch the ball and make it bounce.
        self.__paddle = GRect(paddle_width, paddle_height, y=window_height - paddle_offset)
        self.__paddle_offset = paddle_offset
        self.__paddle.filled = True

        # Center a filled ball in the graphical window.
        self.__ball = GOval(ball_radius * 2, ball_radius * 2, x=window_width / 2
                            - ball_radius, y=window_height / 2 - ball_radius)
        self.__ball.filled = True
        self.__ball_radius = ball_radius

        # Default initial velocity for the ball.
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners.
        onmousemoved(self.__handle_move)

        # Draw bricks in rows and columns.
        self.__brick_width = brick_width
        self.__brick_height = brick_height
        self.__brick_spacing = brick_spacing
        self.__brick_offset = brick_offset
        self.__brick_rows = brick_rows
        self.__brick_cols = brick_cols
        self.__left_bricks = self.__brick_rows * self.__brick_cols

        # Add the elements(bg / wd1 / button / wd2) to start screen.
        self.__window.add(self.__grt_bg)
        self.__window.add(self.__grt_wd1)
        self.__window.add(self.__grt_button)
        self.__window.add(self.__grt_wd2)

        # Scoreboard records the score.
        self.__scores = 0
        self.__scoreboard = GLabel('Score: ' + str(self.__scores), x=0, y=window_height)
        self.__scoreboard.font = 'Courier-18'

        # Click on mouse and start game.
        onmouseclicked(self.start_game)

    # Set up the start screen of the game in this function.
    def start_game(self, event):
        click = self.__window.get_object_at(event.x, event.y)
        b = self.__grt_button
        grt = self.__grt_wd2

        # While the mouse click on the button, start the game.
        if click == b or click == grt and b.x <= event.x <= b.x + b.width and b.y <= event.y <= b.y + b.height:
            self.__window.remove(self.__grt_wd1)        # Remove the greeting words.
            self.__window.remove(self.__grt_wd2)        # Remove the greeting words.
            self.__window.remove(self.__grt_button)     # Remove the start button.
            self.__window.remove(self.__grt_bg)         # Remove the greeting background.
            self.switch = True                          # Turn on the switch.

            # Set the ball on the start position, in the middle of the window.
            self.__window.add(self.__ball, x=self.__window.width/2 - self.__ball.width/2,
                              y=self.__window.height/2 - self.__ball.height/2)
            self.__window.add(self.__paddle)        # Add the paddle to the window.
            self.__draw_bricks()                    # Add the bricks to the window.
            self.__window.add(self.__scoreboard)    # Add the scoreboard to the window.

            pause(300)                              # Delay time serving a ball.

    # Set ball at a random position in certain area, below bricks and above paddle.
    def set_ball_position(self):
        self.__ball.x = random.randint(0, self.__window.width - self.__ball.width)
        self.__ball.y = random.randint(self.__brick_offset + self.__brick_rows *
                                       (self.__brick_height + self.__brick_spacing) - self.__brick_spacing,
                                       self.__window.height - self.__paddle_offset - self.__paddle.height
                                       - self.__ball_radius * 2)
        pause(500)                                  # Delay serving a ball

    # Set the ball in random velocity.
    def set_ball_velocity(self):
        if random.random() > 0.5:
            self.__dx = -self.__dx

    # Determine whether the ball is out of the window.
    # Leave the window from the bottom edge / return boolean (True)
    def ball_out(self):
        if self.__ball.y >= self.__window.height:
            return True

    # If the ball is out of bounds, reset 'position' and 'velocity' of ball, and add it to screen.
    def reset_ball(self):
        self.set_ball_position()
        self.set_ball_velocity()
        self.__window.add(self.__ball)

    # Move ball as animation in velocity of dx and dy.
    def move_ball(self):
        if self.switch:
            self.__ball.move(self.__dx, self.__dy)

    # Check whether the ball collides with walls, then bounce back.
    def wall_collisions(self):
        # Ball collides with up right edge and left edge.
        if self.__ball.x <= 0 or self.__ball.x >= self.__window.width - self.__ball.width:
            self.__dx = -self.__dx

        # Ball collides with upper edge.
        if self.__ball.y <= 0:
            self.__dy = -self.__dy

    # Check whether the ball collides with paddle or bricks, then bounce back.
    def check_for_collisions(self):
        if self.switch:             # if the game starts:
            # Set b1, b2, b3, b4 as four corners of ball.
            b1 = self.__window.get_object_at(self.__ball.x, self.__ball.y)
            b2 = self.__window.get_object_at(self.__ball.x + self.__ball_radius * 2, self.__ball.y)
            b3 = self.__window.get_object_at(self.__ball.x, self.__ball.y + self.__ball_radius * 2)
            b4 = self.__window.get_object_at(self.__ball.x + self.__ball_radius * 2,
                                             self.__ball.y + self.__ball_radius * 2)

            # Detecting whether four corners of ball collides with:
            if b1 is not None or b2 is not None or b3 is not None or b4 is not None:
                # Collides with paddle.
                if b1 is self.__paddle or b2 is self.__paddle or b3 is self.__paddle or b4 is self.__paddle:
                    # Avoid ball stick to paddle.
                    if self.__ball.y + self.__ball_radius*2 >= self.__paddle.y:
                        self.__ball.y = self.__paddle.y - self.__ball_radius*2
                        self.set_ball_velocity()
                        if self.__dy > 0:
                            self.__dy = -self.__dy

                # Collides with scoreboard, then pass.
                elif b1 is self.__scoreboard or b2 is self.__scoreboard or \
                        b3 is self.__scoreboard or b4 is self.__scoreboard:
                    pass

                # Collides with brick / remove the brick / bounce back.
                else:
                    if b1 is not None and b1 is not self.__scoreboard:
                        self.__window.remove(b1)    # Remove a brick while colliding with a brick.
                        self.__left_bricks -= 1     # Minus 1 while colliding with a brick.
                        self.__scores += 10         # Add 10 scores while colliding with a brick.

                    elif b2 is not None and b2 is not self.__scoreboard:
                        self.__window.remove(b2)    # Remove a brick while colliding with a brick.
                        self.__left_bricks -= 1     # Minus 1 while colliding with a brick.
                        self.__scores += 10         # Add 10 scores while colliding with a brick.

                    elif b3 is not None and b3 is not self.__scoreboard:
                        self.__window.remove(b3)    # Remove a brick while colliding with a brick.
                        self.__left_bricks -= 1     # Minus 1 while colliding with a brick.
                        self.__scores += 10         # Add 10 scores while colliding with a brick.

                    elif b4 is not None and b4 is not self.__scoreboard:
                        self.__window.remove(b4)    # Remove a brick while colliding with a brick.
                        self.__left_bricks -= 1     # Minus 1 while colliding with a brick.
                        self.__scores += 10         # Add 10 scores while colliding with a brick.

                    self.__scoreboard.text = 'Score: ' + str(self.__scores)  # Refresh score to scoreboard
                    self.set_ball_velocity()        # Reset x velocity of ball.
                    self.__dy = -self.__dy          # Reset y velocity of ball.

    # Draw bricks.
    def __draw_bricks(self):
        for i in range(self.__brick_rows):
            for j in range(self.__brick_cols):
                br1 = GRect(self.__brick_width, self.__brick_height)
                br1.filled = True

                br1.x = (self.__brick_width + self.__brick_spacing) * j
                br1.y = self.__brick_offset + (self.__brick_height + self.__brick_spacing) * i

                rows_in_sec = self.__brick_rows / BRICK_SECTION

                if i <= rows_in_sec - 1:                                # Section 1
                    br1.fill_color = 'red'
                    br1.color = 'red'
                elif rows_in_sec - 1 < i <= rows_in_sec * 2 - 1:        # Section 2
                    br1.fill_color = 'orange'
                    br1.color = 'orange'
                elif rows_in_sec * 2 - 1 < i <= rows_in_sec * 3 - 1:    # Section 3
                    br1.fill_color = 'yellow'
                    br1.color = 'yellow'
                elif rows_in_sec * 3 - 1 < i <= rows_in_sec * 4 - 1:    # Section 4
                    br1.fill_color = 'green'
                    br1.color = 'green'
                else:                                                   # Section 5 and so on.
                    br1.fill_color = 'lightseagreen'
                    br1.color = 'lightseagreen'

                self.__window.add(br1)

    # Handle the movement of paddle with mouse move.
    def __handle_move(self, event):
        if event.x < self.__paddle.width/2:
            self.__paddle.x = 0
        elif event.x > self.__window.width - self.__paddle.width/2:
            self.__paddle.x = self.__window.width - self.__paddle.width
        else:
            self.__paddle.x = event.x - self.__paddle.width / 2

    # If lives <= 0, then game over.
    def game_over(self):
        g_over = GLabel('GAME OVER!')
        g_over.font = 'Courier-25'
        g_over = GLabel('GAME OVER!', self.__window.width/2-g_over.width/2, self.__window.height/2)
        g_over.font = 'Courier-25'
        self.__window.add(g_over)

    # If the bricks are all removed, you win the game.
    def win_game(self):
        if self.__left_bricks <= 0:
            you_win = GLabel('YOU WIN!')
            you_win.font = 'Courier-25'
            you_win = GLabel('YOU WIN!', self.__window.width / 2 - you_win.width / 2, self.__window.height / 2)
            you_win.font = 'Courier-25'
            self.__window.add(you_win)
            return True
