import cv2
import sys
import os

args = sys.argv

def arg_error():
    print("Please provide a valid image path to decode")
    sys.exit(0)

file_name = ''
if(len(args) > 1):
    file_name = args[1]
    try:
        img = cv2.imread(file_name)
    except:
        arg_error()
else:
    arg_error()

# img = np.array(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
decoded_string = ''.join([chr(val) for val in img.flatten()]).rstrip()

# getting filename only from the provided file
decoded_file_name = "decoded-{file}.txt".format(file=os.path.splitext(file_name)[0].split('/')[-1])

with open(decoded_file_name, 'w') as f:
    f.write(decoded_string)

print("Your file is decoded: {path}".format(path=decoded_file_name))