from PIL import Image
import PIL

pic_cnt = 100
basedir = "..."
todir = "..."
for i in range(pic_cnt):
    imgObject = Image.open(basedir + "IMG_" + str(i + 4020) + ".jpg")
    flipedObject = imgObject.transpose(Image.FLIP_TOP_BOTTOM) # vertical flip
    flipedObject.save(todir + "IMG_" + str(i + 4020) + ".jpg")