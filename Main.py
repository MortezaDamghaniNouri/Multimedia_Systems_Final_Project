# This is Pillow library which is used in many parts of the code
from PIL import Image
# This library is used for fetching the arrays of images
import numpy as np
# This library is used for reading the image file
import matplotlib.image as mpimg

import random


# This function prints the input matrix
def matrix_printer(input_matrix):
    length = len(input_matrix)
    i = 0
    while i < length:
        line = ""
        j = 0
        while j < length:
            line += str(input_matrix[i][j] + "    ")
            j += 1
        print(line)
        i += 1


# This function converts RGB input image to grayscale format
def rgb_to_gray(img):
    R = np.array(img[:, :, 0])
    G = np.array(img[:, :, 1])
    B = np.array(img[:, :, 2])
    R = (R * 0.299)
    G = (G * 0.587)
    B = (B * 0.114)
    Avg = (R + G + B)
    grayImage = img

    for i in range(3):
        grayImage[:, :, i] = Avg

    return grayImage


# This function generates the final dithered image
def dither_function(input_grayscale_image_location):
    window_size = int(input("Enter the size of sliding window (for example if it is n * n just enter n): "))
    image = Image.open(input_grayscale_image_location)
    new = image.copy()
    pix = image.load()
    newpix = new.load()
    width, height = image.size

    area = window_size * window_size
    for i in range(width // window_size):  # loop over pixels
        for j in range(height // window_size):  # loop over pixels
            avg = 0
            area_pix = []
            for k in range(window_size):
                for l in range(window_size):
                    area_pix.append((k, l))  # make a list of coordinates within the tile
                    try:
                        avg += pix[window_size * i + k, window_size * j + l][0]
                        newpix[window_size * i + k, window_size * j + l] = (0, 0, 0)  # set everything to black
                    except IndexError:
                        avg += 255 / 2  # just an arbitrary mean value (when were outside of the image)
                        # this is just a dirty trick for coping with images that have
                        # sides that are not multiples of window
            avg = avg / area
            # val = v is the number of pixels within the tile that will be turned white
            val = round(avg / 255 * (area + 0.99) - 0.5)  # 0.99 due to rounding errors
            assert val <= area, 'something went wrong with the val'
            random.shuffle(area_pix)  # randomize pixel coordinates
            for m in range(val):
                rel_coords = area_pix.pop()  # find random pixel within tile and turn it white
                newpix[window_size * i + rel_coords[0], window_size * j + rel_coords[1]] = (255, 255, 255)

    new.save('Images/dog_dithered_new' + str(window_size) + '.jpg')









# Main part of the code starts here
input_image_location = input("Enter the location of the input image(example: Images/Test4.jpg): ")
image = mpimg.imread(input_image_location)
image = image.copy()
gray_image = rgb_to_gray(image)
grayscale_output = Image.fromarray(gray_image)
grayscale_output.save('Grayscale_Input_Image.png')
dither_function('Grayscale_Input_Image.png')






