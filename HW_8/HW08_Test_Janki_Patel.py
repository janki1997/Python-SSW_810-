"""
@author: Janki patel
CWID : 10457365
"""

""" this file contain testing the code which we already made the fuction in another file call here to test it"""

"""This is importing some of the in-built functions"""




import unittest
from datetime import datetime
from typing import List, Dict
from HW08_Janki_Patel import date_arithmetic, file_reader, FileAnalyzer
class Date_Arithmetic(unittest.TestCase):
    def test_date_arithmetic(self) -> None:
        """we will do testing date arithmetic """
        self.assertEqual(date_arithmetic(), (datetime(
            2020, 3, 1, 0, 0), datetime(2019, 3, 2, 0, 0), 241))
        self.assertNotEqual(date_arithmetic(), (datetime(
            2020, 3, 2, 0, 0), datetime(2019, 3, 2, 0, 0), 241))


class File_reader(unittest.TestCase):
    def test_file_reader(self) -> None:
        """ we will test data for file reader """
        self.assertNotEqual([line for line in file_reader(
            "C:/Users/Janki/Desktop/Masterin/Sem-3/CS-810/HW_8/student_majors.txt", 3, "|", True)], [('123', 'Jin He', 'Science'),
                                                                                                     ('234', 'Software Engineering'),
                                                                                                     ('345', 'Benji Cai', 'Software Engineering')])

        self.assertEqual([line for line in file_reader(
            "C:/Users/Janki/Desktop/Masterin/Sem-3/CS-810/HW_8/student_majors.txt", 3, "|", True)], [('123', 'Jin He', 'Computer Science'),
                                                                                                     ('234', 'Nanda Koka', 'Software Engineering'),
                                                                                                     ('345', 'Benji Cai', 'Software Engineering')])


class File_analyzer(unittest.TestCase):
    """ we will test for file analyzer """

    def test_file_analyzer(self) -> None:
        """we will test for file analyzer """

        f_analyzer: FileAnalyzer = FileAnalyzer(
            "C:\\Users\\Janki\\Desktop\\Masterin\\Sem-3\\CS-810\\HW08_test")
        f_dis1: List[Dict[str, int]] = [
            {'class': 0, 'function': 0, 'line': 3, 'char': 57}]
        self.assertEqual(list(f_analyzer.files_summary.values()), f_dis1)

        f_analyzer: FileAnalyzer = FileAnalyzer(
            "C:\\Users\\Janki\\Desktop\\Masterin\\Sem-3\\CS-810\\HW08_test1")
        f_dis1: List[Dict[str, int]] = [
            {'class': 2, 'function': 4, 'line': 25, 'char': 270}]
        self.assertEqual(list(f_analyzer.files_summary.values()), f_dis1)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
