"""
File: fire.py
Name: Yujing Wei
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation
"""


from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param img: The image of the greenland, to be detected whether on fire.
    :return: str, 'img', (the modified image),
             mark the fire area as red;
             turn the rest of area into grayscale.
    """
    img = SimpleImage(filename)
    for pixel in img:
        avg = (pixel.red + pixel.green + pixel.blue) / 3
        if pixel.red > avg * HURDLE_FACTOR:
            # If pixel.red over the hurdle, then turn pixel.red into red to alert!
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            # Grayscale
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return img

# def highlight_fires(img):
#     """
#     :param img: The image of the greenland, to be detected whether on fire.
#     :return: str, 'img', (the modified image),
#              mark the fire area as red;
#              turn the rest of area into grayscale.
#     """
#     for pixel in img:
#         avg = (pixel.red + pixel.green + pixel.blue) / 3
#         if pixel.red > avg * HURDLE_FACTOR:
#             # If pixel.red over the hurdle, then turn pixel.red into red to alert!
#             pixel.red = 255
#             pixel.green = 0
#             pixel.blue = 0
#         else:
#             # Grayscale
#             pixel.red = avg
#             pixel.green = avg
#             pixel.blue = avg
#     return img


def main():
    """
    Input an image and use function 'highlight_fires()'
    to detect the area which is on fire,
    and then turn the fire area into red color to alert,
    make the rest of image into gray scale.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    # Highlight the area on fire with this function.
    highlighted_fire.show()
    original_fire.show()


if __name__ == '__main__':
    main()
