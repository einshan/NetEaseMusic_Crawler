import os


def get_lyrics_path():
    return './lyrics'


def get_lyrics_dict():
    lyrics_dict = {}
    lyricFiles = os.walk(get_lyrics_path())
    for dirpath, dirnames, filenames in lyricFiles:
        for eachFilename in filenames:
            with open("./lyrics/" + eachFilename, "r", encoding="utf-16") as f:
                lyrics_dict[eachFilename] = f.read() + ''
    return lyrics_dict


def get_lyrics_filenames():
    '''
    返回歌词名称列表
    '''
    for _, __, filenames in os.walk(get_lyrics_path()):
        # print(filenames)
        return filenames


def get_stop_words():
    with open('data/stop_words.txt', encoding='utf-8') as f:
        stop_words = f.read().split('\n')
    return stop_words


def load_all_lyrics_into_onelist():
    onelist = []
    lyrics_filename = get_lyrics_filenames()
    for each_filename in lyrics_filename:
        with open(get_lyrics_path() + '/' + each_filename,
                  'r',
                  encoding='utf-16') as f:
                onelist.append(f.read() + '')
    return onelist
