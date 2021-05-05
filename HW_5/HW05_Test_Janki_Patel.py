"""
@author: Janki patel
CWID : 10457365
"""

"""importing methods from "HW05_Janki_Patel.py" and test the all fuction which we defined logic in the another file and test here"""




import unittest
from HW05_Janki_Patel import reverse, substring, find_second, get_lines
class TestString(unittest.TestCase):
    """All test cases"""

    def test_reverse(self) -> None:
        """display reverse of a string"""
        self.assertEqual(reverse('Janki'), 'iknaJ')
        self.assertEqual(reverse('Love'), 'evoL')
        self.assertEqual(reverse('Python'), 'nohtyP')

    def test_substring(self) -> None:
        """find the substring from main string"""
        self.assertEqual(substring('xyz', 'Janki J Patel'), None)
        self.assertEqual(substring('te', 'Janki J Patel'), 10)
        self.assertEqual(substring('123', '456123879'), 3)

    def test_find_second(self) -> None:
        """find second occurence of target"""
        self.assertEqual(find_second(' ', 'jank jan ki'), 8)
        self.assertEqual(find_second('jan', 'janjanki'), 3)
        self.assertEqual(find_second('a1ba', 'a1ba1bacc'), 3)
        self.assertNotEqual(find_second('l', 'hello world'), 8)

    def test_get_lines(self) -> None:
        """performing reading lines in the file which we deine the path and save it in the fileName"""
        fileName = 'C:\\Users\\Janki\\Desktop\\Masterin\\Sem-3\\CS-810\\HW_5\\HW05_test.txt'
        output = ['<line0>', '<line1>', '<line2>',
                  '<line3.1 line3.2 line3.3>', '<line4.1 line4.2>',
                  '<line5>', '<line6>']
        result = list(get_lines(fileName))
        self.assertEqual(result, output)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
