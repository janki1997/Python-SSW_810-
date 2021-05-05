
"""
@author: Janki patel
CWID : 10457365
"""
"""in this file we will test all the fuction which we make in the HW04_Janki_Patel and that file we will import it"""


import random
import unittest
from typing import Iterator, List, Tuple
from HW04_Janki_Patel import count_vowels,last_occurrence,my_enumerate
# PART 1
    
class CountVowelsTest(unittest.TestCase):
    def test_count_vowels(self):
        """ testing count vowels in the string"""
        self.assertEqual(count_vowels('hello Janki'), 4)
        self.assertEqual(count_vowels('aeiou'), 5)
        self.assertEqual(count_vowels('python'), 1)
     

        
# PART 2
    
class FindLastTest(unittest.TestCase):
    """this method define that how last occurrence work and that logic work properly or not"""
    def test_last_occurrence(self) -> None:
        """define the string which we will test it"""
        j1 : str='#'
        j2 : str='Janki patel'
        seq=['testcase','@@','#','Janki patel']
        """test that fuction which gives you result this is okey or not"""
        self.assertEqual(last_occurrence(j1,seq), 2)
        """try that testcase with list in numbers"""
        self.assertTrue(last_occurrence(12, [3,55,12,66]), 2)
        self.assertEqual(last_occurrence('p', 'aPple'), 2)
        self.assertEqual(last_occurrence(j2,seq), 3)
       
        
  


# PART 4

class EnumerateTest(unittest.TestCase):
    def test_enumerate_list(self) -> None:
        """ test my_enumerate by storing the results in a list """
        self.assertEqual(list(my_enumerate('Janki Patel')), list(enumerate('Janki Patel')))
        """test that in one side it has janki patel but in another side it has blank string so this is not equla function"""
        self.assertNotEqual(list(my_enumerate('Janki Patel')), list(enumerate('')))
        self.assertNotEqual(list(my_enumerate('Janki')), list(enumerate('Janak')))
        

        
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)