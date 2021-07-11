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
            line += str(input_matrix[i][j])  + "    "
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


# This function generates dither matrix according to the user input windows size
def dither_matrix_generator(input_window_size):

    if input_window_size == 2:
        return [[0, 2], [3, 1]]
    previous_level_dither_matrix = dither_matrix_generator(input_window_size / 2)
    output_matrix = []
    i = 0
    while i < input_window_size / 2:
        row = []
        row_in_previous_level_dither_matrix = i % 4
        for j in previous_level_dither_matrix[row_in_previous_level_dither_matrix]:
            row.append(j * 4)
        for j in previous_level_dither_matrix[row_in_previous_level_dither_matrix]:
            row.append(j * 4 + 2)
        output_matrix.append(row)
        i += 1
    i = input_window_size / 2
    while i < input_window_size:
        row = []
        row_in_previous_level_dither_matrix = int(i % 4)
        for j in previous_level_dither_matrix[int(row_in_previous_level_dither_matrix % (input_window_size / 2))]:
            row.append(j * 4 + 3)
        for j in previous_level_dither_matrix[int(row_in_previous_level_dither_matrix % (input_window_size / 2))]:
            row.append(j * 4 + 1)
        output_matrix.append(row)
        i += 1

    return output_matrix


# This function generates the final dithered image
def dither_function(input_grayscale_image_location):
    window_size = int(input("Enter the size of sliding window (for example if it is n * n just enter n and n should be a power of 2): "))
    dither_matrix = dither_matrix_generator(window_size)
    matrix_printer(dither_matrix)













# Main part of the code starts here
input_image_location = input("Enter the location of the input image(example: Images/Test4.jpg): ")
image = mpimg.imread(input_image_location)
image = image.copy()
gray_image = rgb_to_gray(image)
grayscale_output = Image.fromarray(gray_image)
grayscale_output.save('Grayscale_Input_Image.png')
dither_function('Grayscale_Input_Image.png')








