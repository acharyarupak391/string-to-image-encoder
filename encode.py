import cv2
import  numpy as np
import sys
import os

args = sys.argv

def arg_error():
    print("Please provide a valid text file path")
    sys.exit(0)

string = ""
file_name = ''
if(len(args) > 1):
    file_name = args[1]
    try:
        with open(file_name, "r") as f:
            string = f.read()
    except:
        arg_error()
else:
    arg_error()

arr = [ord(char) for char in string]

HEIGHT = 100
fill_len = (3 * HEIGHT) - int(len(arr) % (3 * HEIGHT))
arr.extend([32] * fill_len)

np_array = np.array(arr)

WIDTH = int(len(np_array) / (3 * HEIGHT))
reshaped = np_array.reshape(HEIGHT, WIDTH, 3)

# getting filename only from the provided file
image_name = "{img}.png".format(img=os.path.splitext(file_name)[0].split('/')[-1])
cv2.imwrite(image_name, reshaped)

print("Your file is saved as encoded image: {path}".format(path=image_name))
