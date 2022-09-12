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


def GetThisDir():
    return os.path.abspath(".")


def GetImageNameInFile():
    """
    :rtype: list
    """
    return os.listdir(GetThisDir() + "\\Image")


def main():
    print(GetImageNameInFile())
    print(GetImageNameInFile().__len__())


if __name__ == '__main__':
    main()