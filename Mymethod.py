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

def GetImageNameInFile(file_name: str):
    """
    :rtype: list
    """
    return os.listdir(GetThisDir() + "\\" + file_name)

def TransImageFileToUE(image_name, index: int):
    """
    将输入的路径转换成UE的文件路径

    :param image_name: 输入的图片名,一般情况下的格式是 {图片名字}.png
    :param index: 根据index不同返回不同的文件路径
    :return: 对应的UE文件
    :rtype: str
    """
    if image_name == '':
        return "None"
    if index == 0:
        return "Game\\DialogSystem\\BackgroundImage\\" + image_name
    elif index == 1:
        return "Game\\DialogSystem\\CharacterImage\\" + image_name
    else:
        return "Game\\DialogSystem\\AvatarImage\\" + image_name
