"""
@author: Janki patel
CWID : 10457365
"""

""" this file contain testing the code which we already made the fuction in another file call here to test it"""




import unittest
from HW06_Janki_Patel import list_copy, list_intersect, list_difference, remove_vowels, check_pwd, Donutqueue
class List_copy(unittest.TestCase):
    def test_list_copy(self):
        """test case for copy of list as it is equal or not"""
        self.assertEqual(list_copy(['A', '2', '3']), ['A', '2', '3'])
        self.assertEqual(list_copy(['a', 's', 'd']), ['a', 's', 'd'])
        self.assertEqual(list_copy([1, 2, 3]), [1, 2, 3])


class List_intersect(unittest.TestCase):
    def test_list_intersect(self):
        """ in that test case for intersection of two list which we define """
        self.assertEqual(list_intersect(
            ['b', 'a', 'c'], ['4', 'a', '6']), ['a'])
        self.assertEqual(list_intersect(
            ['1', 'b', '5'], ['b', '1', 'd']), ['1', 'b'])
        self.assertEqual(list_intersect(['4', '5', '6'], []), [])
        self.assertEqual(list_intersect(
            ['1', '9', '3'], ['6', '1']), ['1'])
        self.assertEqual(list_intersect(['1', '2', '3'], ['a', 'c']), [])


class List_difference(unittest.TestCase):
    def test_list_difference(self):
        """in that test case for list difference of two different list"""
        self.assertEqual(list_difference(
            ['a', 'b', 'c'], ['1', 'b', 'd']), ['a', 'c'])
        self.assertEqual(list_difference(['1', '2', '3'], [
                         '4', '5', '6']), ['1', '2', '3'])
        self.assertEqual(list_difference(['a', 'b', 'c'], ['a', 'b', 'c']), [])
        self.assertEqual(list_difference([], ['x', 'y', 'z']), [])


class Remove_vowels(unittest.TestCase):
    def test_remove_vowels(self):
        """in this test case it removing all vowels in the string where the word beging with vowel"""
        self.assertEqual(remove_vowels(
            'My name is janki'), 'My name janki')
        self.assertEqual(remove_vowels(
            'my dog'), 'my dog')
        self.assertEqual(remove_vowels('arjun'), '')

        self.assertEqual(remove_vowels('usual identity'), '')


class Check_pwd(unittest.TestCase):
    def test_check_password(self):
        """in this test case it check for password is right or wrong"""
        self.assertTrue(check_pwd('3JankiPatel'))
        self.assertTrue(check_pwd('375JAnmom'))
        self.assertFalse(check_pwd(''))
        self.assertTrue(check_pwd('7JAn'))
        """try for less then 4 word"""
        self.assertFalse(check_pwd('4As'))
        self.assertFalse(check_pwd('09'))


class DonutQueueTest(unittest.TestCase):
    """in this test case it check donut queue"""

    def test_queue(self):
        dq = Donutqueue()
        self.assertIsNone(dq.next_customer())
        dq.arrive("Janki", False)
        dq.arrive("Foi", False)
        dq.arrive("Prof  jagu", True)
        self.assertEqual(dq.waitinglist(), "Prof  jagu, Janki, Foi")
        dq.arrive("Nishit", True)

        self.assertEqual(dq.waitinglist(), "Prof  jagu, Nishit, Janki, Foi")
        dq.arrive("Dhruvil", True)
        self.assertEqual(dq.waitinglist(),
                         "Prof  jagu, Nishit, Dhruvil, Janki, Foi")
        self.assertEqual(dq.next_customer(), "Prof  jagu")
        self.assertEqual(dq.next_customer(), "Nishit")
        self.assertEqual(dq.waitinglist(), "Dhruvil, Janki, Foi")
        self.assertEqual(dq.next_customer(), "Dhruvil")
        self.assertEqual(dq.next_customer(), "Janki")
        self.assertEqual(dq.waitinglist(), "Foi")
        self.assertEqual(dq.next_customer(), "Foi")
        self.assertIsNone(dq.next_customer())


# start from here
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
