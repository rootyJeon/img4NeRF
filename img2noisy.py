#########################
#                       #
# Made by Byungwoo Jeon #
#   Date : 01/17/2023   #
#                       #
#########################

import os
import cv2
import numpy as np
import img2scaling

def scaling_parser():
    import configargparse

    parser = configargparse.ArgumentParser()
    parser.add_argument("--scale", type=bool, default=False,
                        help="Do image scaling")

    return parser

def make_noisy_img():
    file_path = "..."

    for img_name in os.listdir(file_path):
        img_path = ".../images/" + img_name
        save_path = "..." + img_name
        img = cv2.imread(img_path)

        # gaussian noise parameters
        mean, var = 0, 2500
        sigma = var ** 0.5
        gaussian = np.random.normal(mean, sigma, (1000, 1200)) # size of gaussian

        noisy_image = img
        if len(img.shape) == 2:
            noisy_image = img + gaussian
        else:
            noisy_image[1000:2000, 800:2000 , 0] = noisy_image[1000:2000, 800:2000 , 0] + gaussian # H x W x C
            noisy_image[1000:2000, 800:2000 , 1] = noisy_image[1000:2000, 800:2000 , 1] + gaussian # H x W x C
            noisy_image[1000:2000, 800:2000 , 2] = noisy_image[1000:2000, 800:2000 , 2] + gaussian # H x W x C

        cv2.normalize(noisy_image, noisy_image, 0, 255, cv2.NORM_MINMAX, dtype=-1)
        noisy_image = noisy_image.astype(np.uint8)

        '''
        # Show Images 
        imS = cv2.resize(img, (960, 540))
        noisy_imS = cv2.resize(noisy_image, (960, 540))
        
        cv2.imshow("img", imS)
        cv2.imshow("gaussian", gaussian)
        cv2.imshow("noisy", noisy_imS)
    
        #cv2.waitKey(0)
        '''

        cv2.imwrite(save_path, noisy_image)


if __name__ == "__main__":
    parser = scaling_parser()
    args = parser.parse_args()

    make_noisy_img()

    if args.scale is True:
        img2scaling.scaling()
