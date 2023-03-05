import sys
import cv2

args = sys.argv

def arg_error(msg):
    print(msg)
    sys.exit(0)

def get_string_contents(msg):
    if(len(args) > 1):
        file_name = args[1]
        try:
            with open(file_name, "r") as f:
                string = f.read()

            return {
                'string': string,
                'file_name': file_name
            }
        except:
            arg_error(msg)
    else:
        arg_error(msg)

def get_height_arg():
    try:
        def filter_height(arg):
            return 'height' in arg and int(arg.split('=')[-1])

        HEIGHT = int(list(filter(filter_height, args))[0].split('=')[-1])
    except:
        HEIGHT = 100

    return HEIGHT

def get_image_contents(msg):
    if (len(args) > 1):
        file_name = args[1]
        try:
            img = cv2.imread(file_name)

            return {
                'file_name': file_name,
                'img': img
            }
        except:
            arg_error(msg)
    else:
        arg_error(msg)