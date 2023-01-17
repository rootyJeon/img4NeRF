#########################
#                       #
# Made by Byungwoo Jeon #
#   Date : 01/17/2023   #
#                       #
#########################

import os
from PIL import Image

def scaling():
    file_path = "..."
    scale_size = [4, 8] # define scale sizes (x4, x8, ...)

    for scale in scale_size:
        save_file_path = ".../image_" + str(scale)
        # print(save_file_path)
        os.makedirs(save_file_path, exist_ok=True)

        for img_name in os.listdir(file_path):
            img_path = "..." + img_name
            save_image_path = save_file_path + "/" + img_name
            img = Image.open(img_path)
            img_resize = img.resize((int(img.width/scale), int(img.height/scale))) # scale goes to 4 and 8 respectively
            img_resize.save(save_image_path)

if __name__ == "__main__":
    scaling()