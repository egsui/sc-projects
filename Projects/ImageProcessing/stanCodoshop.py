"""
File: stanCodoshop.py
Name: Yujing Wei
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

This project is made for populating image and create the 'ghost' effect.
The 'ghost' effect is to detect 'human' or 'obstacle' in photo and
remove them from photo automatically.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    # Use function below to get color distance for each pixels and return it.
    color_distance = ((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)**(1/2)
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    red = 0                                         # Set up value of initial 'red' as 0.
    green = 0                                       # Set up value of initial 'green' as 0.
    blue = 0                                        # Set up value of initial 'blue' as 0.
    for pixel in pixels:                            # Sum up value of red, green and blue in each pixel.
        red += pixel.red
        green += pixel.green
        blue += pixel.blue
    red /= len(pixels)                              # Get average value of red, green and blue.
    green /= len(pixels)
    blue /= len(pixels)
    return [int(red), int(green), int(blue)]        # Return average value of red, green and blue as a list.


def get_best_pixel(dis_lst, pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    shortest_dis = dis_lst[0]                   # Assign 'dis_lst[0]' to 'shortest_dis' at the very beginning.
    best = ''                                   # Set 'best' as an empty string at the very beginning.
    for i in range(len(dis_lst)):               # Get data from 'dis_lst' and compare their value.
        if dis_lst[i] <= shortest_dis:          # Find out the smallest value(shortest distance)
            best = pixels[i]                    # Assign the same index of data in 'pixels' list to 'best'.
    return best                                 # Return 'best'. (pixel which is in the shortest distance)


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect.
    for i in range(width):
        for j in range(height):                     # Each pixel at (i, j).
            pixels = []                             # Reset the pixels list at different position(i, j).
            for img in images:                      # Each pixel at (i, j) in each image.
                pixel = img.get_pixel(i, j)         # Get specific info of pixel at (i, j) in img_N.
                pixels.append(pixel)
                # 'pixels' now is a list of specific info of pixels at (i, j) in each images.
                # [img1_pixel(i, j), img2_pixel(i, j), ..., imgN_pixel(i, j)]

            avg_rgb_lst = get_average(pixels)       # Average pixels in list(pixels).
            # Return a list [avg_red, avg_green, avg_blue] and assign to avg_rgb_lst.

            dis_lst = []
            for pixel in pixels:                    # Get color distance of pixel in list(pixels).
                dis_lst.append(get_pixel_dist(pixel, avg_rgb_lst[0], avg_rgb_lst[1], avg_rgb_lst[2]))
                # Return a list of color distance of pixels. ex. [0.7, 1, 2]

            # Compare color distance of pixels, find out and return best_pixel.
            best = get_best_pixel(dis_lst, pixels)

            # Assign best_pixel to result at (i, j).
            result.get_pixel(i, j).red = best.red
            result.get_pixel(i, j).green = best.green
            result.get_pixel(i, j).blue = best.blue

    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
