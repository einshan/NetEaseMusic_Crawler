'''
使用整句（最少5个字）进行搜索（线性搜索），不进行关键字提取。
'''

import os
from sys import argv

script, user_input = argv


def searchv2(userInput: str, lyricsDics: dict):
    # print(lyricsDics.items())
    lyricsDics = loadLyrics()
    relatedFiles = []
    for item in lyricsDics.items():
        # 检测用户输入是否在歌词中。
        if userInput in item[1]:
            print(userInput + " find in " + item[0])
            relatedFiles.append(item[0])
    if len(relatedFiles) == 0:
        print(userInput + " NOT FOUND.")
        return False
    return True


def loadLyrics():
    lyricsDics = {}
    lyricFiles = os.walk("./lyrics/")
    for dirpath, dirnames, filenames in lyricFiles:
        for eachFilename in filenames:
            with open("./lyrics/" + eachFilename, "r", encoding="utf-16") as f:
                lyricsDics[eachFilename] = f.read() + ''
    return lyricsDics


if (len(user_input) <= 4):
    print('输入的语句过短！')
else:
    searchv2(user_input, loadLyrics())
