"""
File: blur.py
Name: Yujing Wei
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: str, the image to be blurred
    :return: 'img', the image that had been blurred(RGB values had been adjusted)
    """
    for r in range(img.width):
        for c in range(img.height):
            img_pixel = img.get_pixel(r, c)  # get the position of 'img'
            if (r - 1) < 0:  # Far left column, r = 0
                if (c - 1) < 0:  # Upper left corner, (0,0)
                    img_pixel2 = img.get_pixel(r + 1, c)
                    img_pixel7 = img.get_pixel(r, c + 1)
                    img_pixel8 = img.get_pixel(r + 1, c + 1)
                    times = 3
                    img_pixel.red = (img_pixel2.red + img_pixel7.red + img_pixel8.red) / times
                    img_pixel.green = (img_pixel2.green + img_pixel7.green + img_pixel8.green) / times
                    img_pixel.blue = (img_pixel2.blue + img_pixel7.blue + img_pixel8.blue) / times

                elif (c + 1) > (img.height - 1):  # Bottom left corner, (0,c)
                    img_pixel2 = img.get_pixel(r + 1, c)
                    img_pixel4 = img.get_pixel(r, c - 1)
                    img_pixel5 = img.get_pixel(r + 1, c - 1)
                    times = 3
                    img_pixel.red = (img_pixel2.red + img_pixel4.red + img_pixel5.red) / times
                    img_pixel.green = (img_pixel2.green + img_pixel4.green + img_pixel5.green) / times
                    img_pixel.blue = (img_pixel2.blue + img_pixel4.blue + img_pixel5.blue) / times

                else:  # position on the left edge(except upper left corner and bottom left corner)
                    img_pixel2 = img.get_pixel(r + 1, c)
                    img_pixel4 = img.get_pixel(r, c - 1)
                    img_pixel5 = img.get_pixel(r + 1, c - 1)
                    img_pixel7 = img.get_pixel(r, c + 1)
                    img_pixel8 = img.get_pixel(r + 1, c + 1)
                    times = 5
                    img_pixel.red = (img_pixel2.red + img_pixel4.red + img_pixel5.red +
                                     img_pixel7.red + img_pixel8.red) / times
                    img_pixel.green = (img_pixel2.green + img_pixel4.green + img_pixel5.green +
                                       img_pixel7.green + img_pixel8.green) / times
                    img_pixel.blue = (img_pixel2.blue + img_pixel4.blue + img_pixel5.blue +
                                      img_pixel7.blue + img_pixel8.blue) / times

            elif (r + 1) > (img.width - 1):  # Far right column, r = img.width
                if (c - 1) < 0:  # Upper right corner, (img.width,0)
                    img_pixel1 = img.get_pixel(r - 1, c)
                    img_pixel6 = img.get_pixel(r - 1, c + 1)
                    img_pixel7 = img.get_pixel(r, c + 1)
                    times = 3
                    img_pixel.red = (img_pixel1.red + img_pixel6.red + img_pixel7.red) / times
                    img_pixel.green = (img_pixel1.green + img_pixel6.green + img_pixel7.green) / times
                    img_pixel.blue = (img_pixel1.blue + img_pixel6.blue + img_pixel7.blue) / times

                elif (c + 1) > (img.height - 1):  # Bottom right corner, (img.width,c)
                    img_pixel1 = img.get_pixel(r - 1, c)
                    img_pixel4 = img.get_pixel(r, c - 1)
                    img_pixel6 = img.get_pixel(r - 1, c - 1)
                    times = 3
                    img_pixel.red = (img_pixel1.red + img_pixel4.red + img_pixel6.red) / times
                    img_pixel.green = (img_pixel1.green + img_pixel4.green + img_pixel6.green) / times
                    img_pixel.blue = (img_pixel1.blue + img_pixel4.blue + img_pixel6.blue) / times

                else:  # position on the right edge(except upper right corner and bottom right corner)
                    img_pixel2 = img.get_pixel(r - 1, c)
                    img_pixel4 = img.get_pixel(r, c - 1)
                    img_pixel5 = img.get_pixel(r - 1, c - 1)
                    img_pixel7 = img.get_pixel(r, c + 1)
                    img_pixel8 = img.get_pixel(r - 1, c + 1)
                    times = 5
                    img_pixel.red = (img_pixel2.red + img_pixel4.red + img_pixel5.red +
                                     img_pixel7.red + img_pixel8.red) / times
                    img_pixel.green = (img_pixel2.green + img_pixel4.green + img_pixel5.green +
                                       img_pixel7.green + img_pixel8.green) / times
                    img_pixel.blue = (img_pixel2.blue + img_pixel4.blue + img_pixel5.blue +
                                      img_pixel7.blue + img_pixel8.blue) / times

            elif (c - 1) < 0:  # Upper edge column, c = 0
                if r != 0 or r != img.width:  # except the corners
                    img_pixel1 = img.get_pixel(r - 1, c)
                    img_pixel2 = img.get_pixel(r + 1, c)
                    img_pixel6 = img.get_pixel(r - 1, c + 1)
                    img_pixel7 = img.get_pixel(r, c + 1)
                    img_pixel8 = img.get_pixel(r + 1, c + 1)
                    times = 5
                    img_pixel.red = (img_pixel1.red + img_pixel2.red + img_pixel6.red +
                                     img_pixel7.red + img_pixel8.red) / times
                    img_pixel.green = (img_pixel1.green + img_pixel2.green + img_pixel6.green +
                                       img_pixel7.green + img_pixel8.green) / times
                    img_pixel.blue = (img_pixel1.blue + img_pixel2.blue + img_pixel6.blue +
                                      img_pixel7.blue + img_pixel8.blue) / times

            elif (c + 1) > (img.height - 1):  # Bottom edge column, c = img.height
                if r != 0 or r != img.width:  # except the corners
                    img_pixel1 = img.get_pixel(r - 1, c)
                    img_pixel2 = img.get_pixel(r + 1, c)
                    img_pixel3 = img.get_pixel(r - 1, c - 1)
                    img_pixel4 = img.get_pixel(r, c - 1)
                    img_pixel5 = img.get_pixel(r + 1, c - 1)
                    times = 5
                    img_pixel.red = (img_pixel1.red + img_pixel2.red + img_pixel3.red +
                                     img_pixel4.red + img_pixel5.red) / times
                    img_pixel.green = (img_pixel1.green + img_pixel2.green + img_pixel3.green +
                                       img_pixel4.green + img_pixel5.green) / times
                    img_pixel.blue = (img_pixel1.blue + img_pixel2.blue + img_pixel3.blue +
                                      img_pixel4.blue + img_pixel5.blue) / times

            else:  # position in the middle of img, which is not on edge
                img_pixel1 = img.get_pixel(r - 1, c)
                img_pixel2 = img.get_pixel(r + 1, c)
                img_pixel3 = img.get_pixel(r - 1, c - 1)
                img_pixel4 = img.get_pixel(r, c - 1)
                img_pixel5 = img.get_pixel(r + 1, c - 1)
                img_pixel6 = img.get_pixel(r - 1, c + 1)
                img_pixel7 = img.get_pixel(r, c + 1)
                img_pixel8 = img.get_pixel(r + 1, c + 1)
                times = 8

                img_pixel.red = (img_pixel1.red + img_pixel2.red + img_pixel3.red +
                                 img_pixel4.red + img_pixel5.red + img_pixel6.red +
                                 img_pixel7.red + img_pixel8.red) / times
                img_pixel.green = (img_pixel1.green + img_pixel2.green + img_pixel3.green +
                                   img_pixel4.green + img_pixel5.green + img_pixel6.green +
                                   img_pixel7.green + img_pixel8.green) / times
                img_pixel.blue = (img_pixel1.blue + img_pixel2.blue + img_pixel3.blue +
                                  img_pixel4.blue + img_pixel5.blue + img_pixel6.blue +
                                  img_pixel7.blue + img_pixel8.blue) / times
    return img


def main():
    """
    Input image as 'old_image' to be blurred;
    Results: show 'old_image' and 'blurred_img'
    """
    old_img = SimpleImage("images/smiley-face.png")  # Input the image to be blurred
    old_img.show()

    blurred_img = blur(old_img)  # blur old_image with this function
    for i in range(3):  # times to blur
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
