"""
File: green_screen.py
Name: Yujing Wei
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in ReyGreenScreen.png
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    Erase the green screen in figure_img and
    combine the result 'figure' with 'space_ship'.
    :param background_img: the background image to place 'figure'
    :param figure_img: the figure with green screen,
                       erase the green screen in image with this function
    :return: 'figure_img', the 'figure'(without green screen) is placed on the background img.
    """
    for y in range(figure_img.height):
        for x in range(figure_img.width):
            pixel = figure_img.get_pixel(x, y)
            bigger = max(pixel.red, pixel.blue)  # returns the one that is bigger
            if pixel.green > bigger * 2:  # green screen
                pixel_bg = background_img.get_pixel(x, y)
                pixel.red = pixel_bg.red
                pixel.blue = pixel_bg.blue
                pixel.green = pixel_bg.green
    return figure_img


def main():
    """
    Erase the green screen in 'images/ReyGreenScreen.png' and
    combine the result('figure') with 'space_ship'.
    Show the result image.
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)  # erase the green screen and combine 'space_ship' and 'figure'
    result.show()


if __name__ == '__main__':
    main()
