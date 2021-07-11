from PIL import Image
import numpy as np
import matplotlib.image as mpimg



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

image = mpimg.imread("Images/Test4.jpg")
image = image.copy()
# print(str(image.flags))
# image.setflags(write=1)
gray_image = rgb_to_gray(image)
to_save = Image.fromarray(gray_image)
to_save.save('Images/greyscale33.png')

















































