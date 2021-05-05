"""in this file we import the file where we write our logic for this program an import that file here to test that code that if that code working properly
@author: Janki patel
CWID : 10457365
"""

import unittest
from HW03_Janki_Patel import Fraction

class TestFraction(unittest.TestCase):
    """ test class Fraction  where all the fuction"""
    def test_init(self):
        """ check numinator and denominator are set correctly or not """
        f: Fraction = Fraction(5, 6)
        self.assertEqual(f.n, 5)
        self.assertEqual(f.dn, 6)
        
    def test_init_exception(self):
        """ check that ZeroDivisionError is occure when appropriate """
        with self.assertRaises(ZeroDivisionError):
            Fraction(5,0)
    def test_str(self):
        "check that pass the string is that string or not"
        fraction:Fraction=Fraction(5,6)
        self.assertEqual(str(fraction),"5/6")
        
    def test_addMethod(self):
        """ check Fraction addition in 2 operands"""
        f12: Fraction = Fraction(1, 2)
        f14: Fraction = Fraction(1, 4)
        """test that fuction which gives you result"""
        self.assertEqual((f12 + f14).simplify(), Fraction(3, 4))
        self.assertEqual(f14, Fraction(1, 4))  
    def test_3operands_inadd(self):
        """ check Fraction with 3 operands """
        f12: Fraction = Fraction(1, 2)
        f14: Fraction = Fraction(1, 4)
        f48: Fraction = Fraction(4, 8)
        """test that fuction which gives you result"""
        self.assertTrue((f12 + f14 + f48).simplify() == Fraction(5,4 ))

        
    def test_subMethod(self):
        """ check Fraction subtraction in 2 operands """
        f12: Fraction = Fraction(1, 2)
        f14: Fraction = Fraction(1, 4)
        """test that fuction which gives you result"""
        self.assertTrue((f12 - f14).simplify(), Fraction(-1, 4))
        self.assertEqual(f12, Fraction(1, 2))  
    def test_3operands_insub(self):
        """ check Fraction with more than two operands in subtraction """
        f12: Fraction = Fraction(1, 2)
        f14: Fraction = Fraction(1, 4)
        f38: Fraction = Fraction(3, 8)
        """test that fuction which gives you result"""
        self.assertTrue((f12 - f14 - f38).simplify(), Fraction(-1, 8))

        
    def test_mulMethod(self):
        """ check Fraction multification in 2 operands"""
        f12: Fraction = Fraction(1, 2)
        f44: Fraction = Fraction(4, 4)
        """test that fuction which gives you result"""
        self.assertTrue((f12 * f44).simplify(), Fraction(4, 8))
        self.assertEqual(f44, Fraction(4, 4))  
    def test_3operands_inmul(self):
        """check Fraction with more 3 operands multi """
        f12: Fraction = Fraction(1, 2)
        f14: Fraction = Fraction(1, 4)
        f44: Fraction = Fraction(4, 4)
        """test that fuction which gives you result"""
        self.assertTrue((f12 * f14 * f44).simplify() == Fraction(1, 8))

        
    def test_divMethod(self):
        """ check Fraction division in 2 operands """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        """test that fuction which gives you result"""
        self.assertTrue((f12 / f34).simplify(), Fraction(2, 3))
        self.assertEqual(f12, Fraction(1, 2))
        
        with self.assertRaises(ZeroDivisionError):
            Fraction(4,8)/Fraction(0,8)

        
    def test_3operands_indiv(self):
        """check Fraction with more than two operands division """
        f12: Fraction = Fraction(1, 2)
        f48: Fraction = Fraction(4, 8)
        f44: Fraction = Fraction(4, 4)
        """test that fuction which gives you result"""
        self.assertTrue((f12 / f48 / f44).simplify() == Fraction(1,1))

        
    def test_neMethod(self):
        """ check Fraction not equal """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f48: Fraction = Fraction(4, 8)
        # f48: Fraction = Fraction(4, 8)
        """test that fuction which gives you result"""
        self.assertEqual(f12 != f34, True)
        self.assertEqual(f48 != f48, False)

        
    def test_ltMethod(self):
        """ check Fraction is less then or not """
        f12: Fraction = Fraction(1, 2)
        f14: Fraction = Fraction(1, 4)
        """test that fuction which gives you result"""
        self.assertTrue(f14 < f12)
        self.assertFalse(f12 < f14)

        
    def test_leMethod(self):
        """ check Fraction  is less then or equal  """
        f12: Fraction = Fraction(1, 2)
        f14: Fraction = Fraction(1, 4)
        """test that fuction which gives you result"""
        self.assertTrue(f14 <= f12)
        self.assertTrue(f14 <= f14)
        self.assertFalse(f12 <= f14)

        
    def test_gtMethod(self):
        """ check Fraction is greater then or not"""
        f12: Fraction = Fraction(1, 2)
        f14: Fraction = Fraction(1, 4)
        """test that fuction which gives you result"""
        self.assertTrue(f12 > f14)
        self.assertFalse(f14 > f12)
        

        
    def test_geMethod(self):
        """ check  Fraction is greater then or equal """
        f12: Fraction = Fraction(1, 2)
        f14: Fraction = Fraction(1, 4)
        """test that fuction which gives you result"""
        self.assertTrue(f12 >= f14)
        self.assertFalse(f14 >= f12)
        self.assertTrue(f12 >= f12)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)