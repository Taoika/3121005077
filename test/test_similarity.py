import unittest
from similarity import is_html, extraction_text, clean, participle, calc_similarity
from filehandle import read_file


class TestSimilarity(unittest.TestCase):
    def test_is_html(self):
        res = is_html(read_file('D:/资料/学习资料/计算机/软件工程/2023/论文查重程序测试样例/orig_0.8_dis_1.txt'))
        self.assertTrue(res)

    def test_not_html(self):
        res = is_html(read_file('D:/资料/学习资料/计算机/软件工程/2023/论文查重程序测试样例/orig.txt'))
        self.assertFalse(res)

    def test_extraction_text(self):
        text = extraction_text(
            read_file('D:/资料/学习资料/计算机/软件工程/2023/论文查重程序测试样例/orig_0.8_dis_1.txt'))
        self.assertIsInstance(text, str)

    def test_clean(self):
        test_list = ['111', '我是谁', 'abc', '/n/n', '%7&']
        rea_list = clean(test_list)
        self.assertEqual(rea_list, ['111', '我是谁', 'abc'])

    def test_participle(self):
        text = '一位真正的作家永远只为内心写作，'
        should_res_list = ['一位', '真正', '的', '作家', '永远', '只', '为', '内心', '写作', '，']
        rel_res_list = participle(text)
        self.assertEqual(rel_res_list, should_res_list)

    def test_calc_similarity(self):
        list1 = ['一位', '真正', '的', '作家', '永远', '只', '为', '内心', '写作']
        list2 = ['一位', '真正', '的', '作家', '永远', '只', '为', '内心', '写作']
        res = calc_similarity(list1, list2)
        self.assertEqual(round(res, 2), 1)