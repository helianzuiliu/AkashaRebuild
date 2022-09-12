#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

import os.path
from PIL import Image, ImageTk


def GetImage(path, width, height):
    im = Image.open(path).resize((width, height))
    return ImageTk.PhotoImage(im)


a = "F:\\幻书启世录\\物料资源\\BG CG\\"
images = os.listdir(a)
image_dict = {}
for image in images:
    # b=GetImage(a + image, 800, 600)
    # image_dict[image] = b #  我麻了
    print(a + image)
