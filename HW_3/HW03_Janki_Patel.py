
"""
@author: Janki patel
CWID : 10457365
    Implement a class for fractions that supports addition, subtraction, multiplication, and division
    
    This file provides a framework for HW02 that you can use to get organize your solution.
    You may also use a different solution.
"""

class Fraction:
    """ Support addition, subtraction, multiplication, and division of fractions
        with a simple algorithm
    """
    def __init__(self, n: float, dn: float) -> None:
        """ store num and denom
            Raise ZeroDivisionError on 0 denominator 
        """
        """defien the variable for the fuction which we will use in the fuction
        when denomenator is 0 then it will display error """
        if dn == 0:
            raise ZeroDivisionError
       
        self.n: float = n
        self.dn: float = dn

        if self.dn <0 :
            self.n = self.n * -1
            self.dn = self.dn * -1
        
     
        
    def __str__(self) -> str:
        """ return a String to display fractions """

        return f"{self.n}/{self.dn}"

    def simplify(self)-> "Fraction":
        
        n1: float = self.n
        d1: float = self.dn
        temp:float = 0
        """check that denomenator should not be zero"""
        while d1 != 0:
            temp , d1 = d1,(n1 % d1)
            n1 = temp
        """make one object and store temp value in that"""
        new: float=temp
        """that new object it will divide with numerator and denomenator as well"""
        num2 = self.n / new
        denom2 = self.dn / new
        """return that fraction with num2 and denom2"""
        return Fraction(num2,denom2)
       
    def __add__(self, other: "Fraction") -> "Fraction":
        """ Add two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        """code for the plus when we have value on that which value do which operation with which another value and result should be in float """
        num :float = (other.dn * self.n) + (self.dn * other.n)
        denom : float= self.dn * other.dn
        """store the value"""
        Fraction1 = Fraction(num,denom)
        result_plus = Fraction1
        """retuen the value which store the answer"""
        return result_plus
      
        
    def __sub__(self, other: "Fraction") -> "Fraction":
        """code for the minus when we have value on that which value do which operation with which another value and result should be in float"""
        num : float= (other.dn * self.n) - (self.dn * other.n)
        denom : float= self.dn * other.dn
        """store the value"""
        Fraction1 = Fraction(num,denom)
        result_minus = Fraction1
        """return the answer"""
        return result_minus

        
    def __mul__(self, other: "Fraction") -> "Fraction":
       
        """code for the times when we have value on that which value do which operation with which another value """
        """result should be in float"""
        num : float= self.n * other.n
        denom :float = self.dn * other.dn
        """store the value"""
        Fraction1 = Fraction(num,denom)
        result_times = Fraction1
        """return the answer"""
        return result_times
  
        
    def __truediv__(self, other: "Fraction") -> "Fraction":
        
        """code for the plus when we have value on that which value do which operation with which another value """
        """ result should be in float"""
        num :float= self.n * other.dn
        denom :float= other.n * self.dn
        """store the value"""
        Fraction1 = Fraction(num,denom)
        result_divide = Fraction1
        """return asnwer"""
        return result_divide

        
    def __eq__(self, other: "Fraction")-> bool:
        """ return True/False if the two fractions are equivalent """
        # TODO: implement me
        """return the value when same and we want the result in true or false"""
        if ((self.n * other.dn) == (self.dn * other.n)):
            return True
        else:
            return False


    def __ne__(self, other: "Fraction")-> bool:
        """ return True/False if the two fractions are not equivalent """
        if ((self.n * other.dn) != (self.dn * other.n)):
            return True
        else:
            return False


    def __lt__(self, other: "Fraction")->bool:
        """ return True/False if the two fractions less than to another one """
        if((self.n/self.dn)<(other.n/other.dn)):
            return True
        else:
            return False


    def __le__(self, other: "Fraction")->bool:
        """ return True/False if the two fractions less than or equal to another one """
        if((self.n/self.dn)<=(other.n/other.dn)):
            return True
        else:
            return False

    def __gt__(self, other: "Fraction")->bool:
        """ return True/False if the two fractions greater than to another one """
        if((self.n/self.dn)>(other.n/other.dn)):
            return True
        else:
            return False

    def __ge__(self, other: "Fraction")->bool:
        """ return True/False if the two fractions greate than or equal to another one """
        if((self.n/self.dn)>=(other.n/other.dn)):
            return True
        else:
            return False

        
def get_number(prompt: str) -> float:
    """ read and return a number from the user.
        Loop until the user provides a valid number.
    """
    while True:
        inp: str = input(prompt)
        try:
            return float(inp)
        except ValueError:
            print(f"Error: '{inp}' is not a number. Please try again...")

def get_fraction() -> Fraction:
    """ Ask the user for a numerator and denominator and return a valid Fraction """
    while True:
        """Ask the user to enter their number which they want to do operands """
        n:float = get_number('enter your nume')
        dn: float = get_number('enter your denom')
        """in franction when denomator is 0 on that it will say it is not valid and ask for another number"""
        if dn == 0:
            print('d cannot be zero')
            dn:float = int(input('enter your denom'))
        """store the value of the operation""" 
        fraction=Fraction(n,dn)
        return fraction

    

