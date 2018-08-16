# 网易云音乐歌词爬虫 + 利用歌词检索相关歌曲

## 项目进展情况

### 爬虫部分

完成情况：完成爬取歌词文件，利用歌曲id爬取对应歌手信息未完成。

对应的文件是：NEM_spider，爬取的歌词放在 "./NEMCrawler/lyrics" 目录下。

程序流程：

1. 对与给定的歌单爬取歌手信息，并进行歌手去重复。
2. 对于爬取的歌手列表中的每一个歌手，利用其 id 搜索其热门歌曲（在网易云音乐，搜索某个歌手页面下面显示的热门歌曲，最多有50个）。
3. 利用歌曲id，来爬取歌词，并存文件中。

### 检索部分

* searchv1 使用 tfidf 值来进行排名，目前只做到计算出 tfidf 值部分，排名部分未完成。
* searchv2 直接使用整句进行匹配，已完成。
* search 结合了 searchv1 和 searchv2 的功能，如果整句匹配成功，则其对应的歌词文件排名最靠前，未完成。

### 可演示功能

* `python searchv2.py '月亮代表我的心'`
* `python searchv1.py` (输出是 tfidf值 矩阵）

## 项目讨论记录：

### 使用各种粒度的查询条件？

#### 以一整句作为查询条件，例如：

“月亮代表我的心”，而非使用“月亮”进行查询。

这样的影响有：查询过程就是在所有的歌词文件中查找是否出现过这句话，而几乎用不到 TFIDF 算法、分词及 Indexed Searching 技术，而简单的变为匹配问题（甚至都用不到正表达式）。

#### 以关键词作为查询条件，例如：

“月亮” “心”，而非使用“月亮代表我的心"。

这样的影响有：匹配结果不准确，不是很清楚 Indexed Searching 到底该怎么使用。

## 参考文献

[python 怎么从命令行获得输入](https://blog.csdn.net/grozy_sun/article/details/37991793)

[使用 sklearn 计算 tfidf](http://scikit-learn.org/stable/modules/feature_extraction.html)

[分词工具——jieba](https://github.com/fxsjy/jieba)

[python 编码问题](https://segmentfault.com/q/1010000006912134/a-1020000006912397)

[网易云音乐api](https://github.com/darknessomi/musicbox/blob/master/NEMbox/api.py)
