import api
import lyrics_processing
import jieba
from sys import argv

script, user_input = argv
tfidf = lyrics_processing.compute_tfidf()

print('tfidf 值：')
print(tfidf)

print('第一个歌词文件的前 300 个 content word 的 tdidf 值')
print(tfidf[0][:300])

seg_list = jieba.cut(user_input)  # 默认是精确模式
top_ten = []
