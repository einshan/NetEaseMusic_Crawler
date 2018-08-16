import re
import jieba
import api
import os
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer


# 格式化文本，去除无关信息
def format_content(content):
    content = content.replace(u'\xa0', u' ')
    content = re.sub(r'\[.*?\]', '', content)
    content = re.sub(r'\s*作曲.*\n', '', content)
    content = re.sub(r'\s*作词.*\n', '', content)
    content = re.sub(r'.*:', '', content)
    content = re.sub(r'.*：', '', content)
    content = content.replace('\n', ' ')
    return content


def word_segmentation(documents, stop_words):
    # 过滤空格
    filtered_space_documents = []
    for document in documents:
        document = document.replace(' ', '')
        filtered_space_documents.append(document)

    # 使用 jieba 分词对文本进行分词处理
    tokenized_documents = []
    for document in filtered_space_documents:
        seg_list = jieba.cut(document, cut_all=False)
        tokenized_documents.append(list(seg_list))
    # print('分词后的第一个文档：')
    # print(tokenized_documents[0])

    # 去除停用词
    content_word_documents = []
    for document in tokenized_documents:
        content_word_document = []
        for word in document:
            if word not in stop_words:
                content_word_document.append(word)
        content_word_documents.append(' '.join(content_word_document))
    # print('输出去除停用词之后的第一个文档：')
    # print(content_word_documents[0:2])

    return content_word_documents


def preprocessing_lyrics():
    # 去除无用的作曲及作词等信息, 并将处理之后的歌词文件放在 ./lyrics 目录下。
    lyrics_filenames = api.get_lyrics_filenames()
    for file_name in lyrics_filenames:
        with open(api.get_lyrics_path() + '/' + file_name,
                  "r+",
                  encoding="utf-16") as f:
            data = format_content(f.read())
            f.close()
            os.remove(api.get_lyrics_path() + '/' + file_name)
            with open(api.get_lyrics_path() + '/' + file_name,
                      "w",
                      encoding="utf-16") as f:
                # 将处理之后的歌词数据写入
                f.write(data)


def compute_tfidf():
    # 分词及去除停用词处理，并将结果保存在 ./tokenizedLyrics 目录下。
    stop_words = api.get_stop_words()
    documents = api.load_all_lyrics_into_onelist()
    content_word_documents = word_segmentation(documents, stop_words)
    with open('./tokenizedLyrics/' + 'tokenized_lyrics',
              'w',
              encoding='utf-16') as f:
        for content_word_document in content_word_documents:
            f.write('\n'.join(content_word_document))

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(content_word_documents)
    # print(X.shape)
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(X)
    return tfidf
