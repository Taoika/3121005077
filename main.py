import jieba
from bs4 import BeautifulSoup
import re
from gensim import corpora, similarities
import sys


# 分词
def Participle(text):
    seg_list = jieba.lcut(text)  # 默认是精确模式
    return (seg_list)


# 文件读取
def ReadFile(path):
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


# 内容清洗
def Clean(arr):
    result = []
    for item in arr:
        # 仅匹配中英文
        if (re.match(u"[a-zA-Z0-9\u4e00-\u9fa5]", item)):
            result.append(item)
            return result
        else:
            pass

    return result


# 从html中提取文本
def ExtractionText(html):
    # 创建Beautiful Soup对象
    soup = BeautifulSoup(html, 'html.parser')
    # 提取所有的<td>标签
    td_tags = soup.find_all('td')
    textList = []
    # 提取文本内容并存储
    for td in td_tags:
        textList.append(td.text)

    string = ''.join(textList)
    return string


# 判断文本是否html代码
def IsHtml(text):
    soup = BeautifulSoup(text, 'html.parser')
    td_tags = soup.find_all('td')
    if (len(td_tags)):
        return True
    else:
        return False


# 频率计算
def CalcFrequency(text1List1, textList2):
    textList = [text1List1, textList2]
    # 将所有文本中的词语映射到唯一的ID
    dictionary = corpora.Dictionary(textList)
    # 创建一个语料库，将文本转化为词袋（bag-of-words）表示
    corpus = [dictionary.doc2bow(text) for text in textList]
    return dictionary, corpus


# 余弦相似度计算
def CalcSimilarity(text1, text2):
    # 将文本转化为词袋表示的语料库
    dictionary, corpus = CalcFrequency(text1, text2)
    # 创建余弦相似度计算对象
    similarity = similarities.Similarity('-Similarity-index', corpus, num_features=len(dictionary))
    # 将text1转化为词袋表示
    test_corpus_1 = dictionary.doc2bow(text1)
    # 计算余弦相似度
    cos_similarity = similarity[test_corpus_1][1]
    # 返回余弦相似度
    return cos_similarity

# 获取命令行参数
def GetArgs():
    # 命令行参数列表
    args = sys.argv

    if len(args) > 2:
        print("参数1:", args[1])
        print("参数2:", args[2])
        return args[1], args[2]
    elif len(args) < 2:
        print("请提供两个用于比对的文件路径!")

# 主函数
def main():

    path1, path2 = GetArgs()

    original_text1 = ReadFile(path1)  # 原文
    original_text2 = ReadFile(path2)  # html

    text1 = Participle(original_text1)
    text2 = Participle(ExtractionText(original_text2))

    print((CalcSimilarity(text1, text2)))

if __name__ == "__main__":
    main()
