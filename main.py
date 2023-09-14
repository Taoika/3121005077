import jieba
import sys


# 分词
def Participle(text):
    seg_list = jieba.lcut(text)  # 默认是精确模式
    print(seg_list)

# 内容读取模块
def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()

    return text


def main():
    path1 = 'D:/资料/学习资料/计算机/软件工程/2023/论文查重程序测试样例/orig.txt'
    path2 = 'D:/资料/学习资料/计算机/软件工程/2023/论文查重程序测试样例/orig_0.8_add.txt'

    text1 = read_file(path1)
    text2 = read_file(path2)


if __name__ == "__main__":
    main()
