import cv2
import  numpy as np
import sys
import os

from args import get_string_contents, get_height_arg

content = get_string_contents(msg="Please provide a valid text file path")
string = content['string']
file_name = content['file_name']

HEIGHT = get_height_arg()

arr = [ord(char) for char in string]

fill_len = (3 * HEIGHT) - int(len(arr) % (3 * HEIGHT))
arr.extend([32] * fill_len)

np_array = np.array(arr)

WIDTH = int(len(np_array) / (3 * HEIGHT))
reshaped = np_array.reshape(HEIGHT, WIDTH, 3)

# getting filename only from the provided file
image_name = "{img}.png".format(img=os.path.splitext(file_name)[0].split('/')[-1])
cv2.imwrite(image_name, reshaped)

print("The encoded image is saved as: {path}".format(path=image_name))
