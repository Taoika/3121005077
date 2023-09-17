import sys
from filehandle import read_file, write_answer
from similarity import is_html, extraction_text, clean, participle, calc_similarity


# 获取命令行参数
def get_args():
    # 命令行参数列表
    args = sys.argv

    if len(args) > 3:
        return args[1], args[2], args[3]
    elif len(args) <= 3:
        print("请提供两个用于比对的文件路径 以及 一个答案写入的文件路径!")
        return '', ''


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
