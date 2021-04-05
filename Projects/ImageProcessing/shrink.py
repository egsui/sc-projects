"""
File: shrink.py
Name: Yujing Wei
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage
SCALE = 1/2  # scale rate must be > 0 and < 1


def shrink(img):
    """
    :param img: str, the image that going to be shrink.
    :return shrink_img: str, with the condition that had been scaled and
                        its RGB values had been re-distributed from the 'img'.
    """
    # scale the img into a new blank canvas
    shrink_img = SimpleImage.blank(int(img.width * SCALE), int(img.height * SCALE))
    for x in range(shrink_img.width):
        for y in range(shrink_img.height):
            shrink_pixel = shrink_img.get_pixel(x, y)
            r = shrink_pixel.red  # red value of (blank)shrink_img
            g = shrink_pixel.green  # green value of (blank)shrink_img
            b = shrink_pixel.blue  # blue value of (blank)shrink_img
            for i in range(int(1 / SCALE)):
                for j in range(int(1 / SCALE)):
                    # take RGB value from specific range of pixels and add them up
                    img_pixel1 = img.get_pixel((x * (1 / SCALE) + i), (y * (1 / SCALE) + j))
                    r += img_pixel1.red
                    g += img_pixel1.green
                    b += img_pixel1.blue
            # average of the added-up values for shrink_img(x, y)
            shrink_pixel.red = r / (int(1 / SCALE) * int(1 / SCALE))
            shrink_pixel.green = g / (int(1 / SCALE) * int(1 / SCALE))
            shrink_pixel.blue = b / (int(1 / SCALE) * int(1 / SCALE))
    return shrink_img


def main():
    """
    Input 'images/poppy.png' and assign it to 'original', then show it.
    Make 'shrink()' function to scale image and redistribute color values, then show it.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink(original)  # scale image and redistribute color values
    after_shrink.show()


if __name__ == '__main__':
    main()
