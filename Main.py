# This is Pillow library which is used in many parts of the code
from PIL import Image
# This library is used for fetching the arrays of images
import numpy as np
# This library is used for reading the image file
import matplotlib.image as mpimg


# This function converts RGB input image to grayscale format
def rgb_to_gray(img):

        R = np.array(img[:, :, 0])
        G = np.array(img[:, :, 1])
        B = np.array(img[:, :, 2])

        R = (R * 0.299)
        G = (G * 0.587)
        B = (B * 0.114)

        Avg = (R+G+B)
        grayImage = img

        for i in range(3):
           grayImage[:,:,i] = Avg

        return grayImage



# Main part of the code starts here
input_image_location = input("Enter the location of the input image(example: Images/Test4.jpg): ")
image = mpimg.imread(input_image_location)
image = image.copy()
gray_image = rgb_to_gray(image)
grayscale_output = Image.fromarray(gray_image)
grayscale_output.save('Grayscale_Input_Image.png')


















































