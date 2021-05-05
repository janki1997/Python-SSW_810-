"""test all the case  which are import from HW_08_Shraddha_gabani"""
import unittest
from datetime import datetime
from typing import List, Dict
from janki import date_arithmetic, file_reader, FileAnalyzer


class TestDateAndFile(unittest.TestCase):
    """ Test class of the methods """

    def test_date_arithmetic(self):
        """ testing date arithmetic """
        self.assertEqual(date_arithmetic(), (datetime(2020, 3, 1, 0, 0), datetime(2019, 3, 2, 0, 0), 241))

    def test_file_reader(self):
        """test the file reader"""
        path: str = "bad_file_name.txt"

        with self.assertRaises(FileNotFoundError):
            final = [(cwid, name, major) for cwid, name, major in
                      file_reader(path, 3, sep='|', header=True)]

        path: str = 'D://810//student_majors.txt'

        with self.assertRaises(ValueError):  # raise ValueError if field != row_field_count
            final = [(cwid, name, major) for cwid, name, major in
                      file_reader(path, 2, sep='|', header=True)]
        a = list()
        ex = ["('123', 'Jin He', 'Computer Science')", "('234', 'Nanda Koka', 'Software Engineering')",
             "('345', 'Benji Cai', 'Software Engineering')"]

        for items in file_reader('D://810//student_majors.txt', 3, sep='|', header=True):
            a.append(f"{items}")

        self.assertEqual(a, ex)


    def test_file_analyzer(self):
        """ test the file analyzer """
        with self.assertRaises(FileNotFoundError):
            file = FileAnalyzer("doesn't_exist")  # invalid directory
            file.pretty_print()

        file_analyzer: FileAnalyzer = FileAnalyzer("D://810")  # valid directory
        ex: List[Dict[str, int]] = [{'class': 0, 'function': 1, 'line': 18, 'char': 300},
                                        {'class': 4, 'function': 8, 'line': 102, 'char': 2858},\
                                        {'class': 1, 'function': 12, 'line': 159, 'char': 5493},\
                                        {'class': 1, 'function': 17, 'line': 190, 'char': 6490},\
                                        {'class': 1, 'function': 16, 'line': 137, 'char': 4715},\
                                        {'class': 0, 'function': 4, 'line': 59, 'char': 1761},\
                                        {'class': 1, 'function': 3, 'line': 41, 'char': 1606},\
                                        {'class': 0, 'function': 5, 'line': 84, 'char': 2445},\
                                        {'class': 1, 'function': 4, 'line': 37, 'char': 1504},\
                                        {'class': 2, 'function': 14, 'line': 143, 'char': 4764},\
                                        {'class': 1, 'function': 6, 'line': 62, 'char': 2679},\
                                        {'class': 0, 'function': 6, 'line': 67, 'char': 2337},\
                                        {'class': 1, 'function': 5, 'line': 40, 'char': 2125},\
                                        {'class': 1, 'function': 6, 'line': 114, 'char': 4695},\
                                        {'class': 1, 'function': 3, 'line': 65, 'char': 3345}]
        self.assertTrue(list(file_analyzer.files_summary.values()) == ex)
        

        

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)