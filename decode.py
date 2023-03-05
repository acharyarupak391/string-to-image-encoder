import os
from args import get_image_contents

contents = get_image_contents(msg="Please provide a valid image path to decode")
img = contents['img']
file_name = contents['file_name']

# img = np.array(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
decoded_string = ''.join([chr(val) for val in img.flatten()]).rstrip()

# getting filename only from the provided file
decoded_file_name = "decoded-{file}.txt".format(file=os.path.splitext(file_name)[0].split('/')[-1])

with open(decoded_file_name, 'w') as f:
    f.write(decoded_string)

print("The decoded file is saved as: {path}".format(path=decoded_file_name))