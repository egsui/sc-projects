"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3            # Default times(lives) to play the game.


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    # Balls after the first ball are random served.
    while True:
        graphics.move_ball()                # Balls are moved based on this function.
        graphics.check_for_collisions()     # Check whether the ball is colliding with paddle or brick.
        graphics.wall_collisions()          # Check whether the ball is colliding with edges.
        pause(FRAME_RATE)                   # Pause the animation with FRAME_RATE.
        if graphics.ball_out():             # If the ball is out of the bottom edge:
            lives -= 1                      # Minus 1 life.
            if lives > 0:                   # If left lives > 0, play again.
                graphics.reset_ball()       # Reset the ball position.
            else:
                graphics.game_over()        # If left lives <= 0, game over.
                break                       # Stop looping if we've lost all NUM_LIVES lives.
        if graphics.win_game():             # If all bricks are removed, you win.
            break                           # Stop looping while you win.


if __name__ == '__main__':
    main()
