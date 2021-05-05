
"""
@author: Janki patel
CWID : 10457365
"""

""" this file contain testing the code which we already made the fuction in another file call here to test it"""

"""This is importing some of the in-built functions"""



import unittest
from HW07_Janki_Patel import anagrams_lst, anagrams_dd, anagrams_cntr, covers_alphabet, web_analyzer
from collections import defaultdict, Counter
from typing import Any, Optional, List, DefaultDict, Tuple
class Test_anagram_lst(unittest.TestCase):
    def test_anagram_lst(self) -> None:
        """ anagrams using list fuction test cases"""
        self.assertTrue(anagrams_lst('JAnki', 'kiJAn'))
        self.assertTrue(anagrams_lst('DINKY', 'dinky'))
        self.assertFalse(anagrams_lst('Janak', 'Janabc'))
        self.assertFalse(anagrams_lst('Thank you', ''))
        self.assertFalse(anagrams_lst('Thank', '1234'))

    def test_anagrams_dd(self) -> None:
        """anagrams using defaultdictionary fuction test cases"""
        self.assertTrue(anagrams_dd('JAnki', 'kiJAn'))
        self.assertTrue(anagrams_dd('DINKY', 'dinky'))
        self.assertFalse(anagrams_dd(' ', ''))
        self.assertFalse(anagrams_dd('Thank', '1234'))

    def test_anagrams_counter(self) -> None:
        """ anagrams using Counter fuction test cases"""
        self.assertTrue(anagrams_cntr('JAnki', 'kiJAn'))
        self.assertTrue(anagrams_cntr('DINKY', 'dinky'))
        self.assertFalse(anagrams_cntr(' ', ''))
        self.assertFalse(anagrams_cntr('Thank', '1234'))

    def test_covers_alphabet(self) -> None:
        """covering all alphabets fuction test cases"""
        self.assertTrue(covers_alphabet("QWERTYUIOPLKJHGFDSAZXCVBNM"))
        self.assertTrue(covers_alphabet(
            "abcdefghijklmnopqrstuvwxyzjanki is good in python"))
        self.assertTrue(covers_alphabet(
            "The quick brown fox jumps over the lazy dog"))
        self.assertFalse(covers_alphabet("1234567"))
        self.assertFalse(covers_alphabet("xyz"))

    def test_web_analyzer(self) -> None:
        """ web analyser fuction test cases"""
        weblogs: List[Tuple[str, str]] = [
            ('Nanda', 'google.com'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Nanda', 'python.org'),
            ('Fei', 'dzone.com'), ('Nanda', 'google.com'),
            ('Maha', 'google.com'), ]

        summary: List[Tuple[str, List[str]]] = [
            ('dzone.com', ['Fei']),
            ('google.com', ['Maha', 'Nanda']),
            ('python.org', ['Fei', 'Nanda']), ]

        self.assertEqual(web_analyzer(weblogs), summary)


"""program will start from here"""
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
