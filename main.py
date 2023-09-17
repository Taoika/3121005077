import jieba
from bs4 import BeautifulSoup
import re
from gensim import corpora, similarities
import sys


# 获取命令行参数
def get_args():
    # 命令行参数列表
    args = sys.argv

    if len(args) > 3:
        return args[1], args[2], args[3]
    elif len(args) <= 3:
        print("请提供两个用于比对的文件路径 以及 一个答案写入的文件路径!")
        return '', ''


# 文件读取
def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


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
        # 仅匹配中英文
        if re.match(u"[a-zA-Z0-9\u4e00-\u9fa5]", item):
            result.append(item)
        else:
            pass

    return result


# 频率计算
def calc_frequency(text1_list1, text_list2):
    text_list = [text1_list1, text_list2]
    # 映射到唯一的ID
    dictionary = corpora.Dictionary(text_list)
    # 文本转化为词袋（bag-of-words）表示
    corpus = [dictionary.doc2bow(text) for text in text_list]
    return dictionary, corpus


# 余弦相似度计算
def calc_similarity(text1, text2):
    dictionary, corpus = calc_frequency(text1, text2)
    similarity = similarities.Similarity('-Similarity-index', corpus, num_features=len(dictionary))
    test_corpus_1 = dictionary.doc2bow(text1)
    # 计算余弦相似度
    cos_similarity = similarity[test_corpus_1][1]
    return cos_similarity


# 答案写入
def write_answer(path, sim):
    judge = '判定为抄袭' if sim > 0.6 else '不认定为抄袭'
    try:
        with open(path, 'w') as file:
            file.write('相似度:' + '%.2f%%' % (sim * 100))
            file.write('\n' + judge)
        print(f"成功将答案写入文件")
    except IOError as e:
        print(f"写入文件时发生错误：{e}")


# 主函数
def main():
    # 参数获取
    path1, path2, path3 = get_args()
    if path1 == '' or path2 == '' or path3 == '':
        return

    original_text1 = read_file(path1)  # 原文
    original_text2 = read_file(path2)  # html

    # 提取
    if is_html(original_text1):
        text1_pro = extraction_text(original_text1)
    else:
        text1_pro = original_text1

    if is_html(original_text2):
        text2_pro = extraction_text(original_text2)
    else:
        text2_pro = original_text2

    # 分词 清洗
    text1 = clean(participle(text1_pro))
    text2 = clean(participle(text2_pro))

    # 相似度 抄袭判定
    sim = (calc_similarity(text1, text2))

    # 答案写入
    write_answer(path3, sim)


if __name__ == "__main__":
    main()
