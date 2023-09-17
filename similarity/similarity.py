import jieba
from bs4 import BeautifulSoup
import re
from gensim import corpora, similarities


# 从html中提取文本
def extraction_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    td_tags = soup.find_all('td')
    text_list = []
    # 提取文本内容并存储
    for td in td_tags:
        text_list.append(td.text)

    string = ''.join(text_list)
    return string


# 判断文本是否html代码
def is_html(text):
    soup = BeautifulSoup(text, 'html.parser')
    td_tags = soup.find_all('td')
    if len(td_tags):
        return True
    else:
        return False


# 分词
def participle(text):
    seg_list = jieba.lcut(text)  # 默认是精确模式
    return seg_list


# 内容清洗
def clean(arr):
    result = []
    for item in arr:
        # 仅匹配中英文数字
        if re.match(u"[a-zA-Z0-9\u4e00-\u9fa5]", item):
            result.append(item)
        else:
            pass

    return result


# 余弦相似度计算
def calc_similarity(text1, text2):
    text_list = [text1, text2]
    # 映射到唯一的ID
    dictionary = corpora.Dictionary(text_list)
    # 文本转化为词袋（bag-of-words）表示
    corpus = [dictionary.doc2bow(text) for text in text_list]
    similarity = similarities.Similarity('-Similarity-index', corpus, num_features=len(dictionary))
    test_corpus_1 = dictionary.doc2bow(text1)
    # 计算余弦相似度
    cos_similarity = similarity[test_corpus_1][1]
    return cos_similarity
