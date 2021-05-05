#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 12:46:59 2017

@author: jrr

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
        when denomenator is 0 then it will display error"""
        if dn == 0:
            raise ZeroDivisionError
       
        self.n: float = n
        self.dn: float = dn
        
        # TODO: implement me
        
    def __str__(self) -> str:
        """ return a String to display fractions """
        """ TODO: implement me
        display the value of the fraction which we choose to do operation and the value"""

        return f"{self.n}/{self.dn}"
       
    def plus(self, other: "Fraction") -> "Fraction":
        """ Add two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        """code for the plus when we have value on that which value do which operation with which another value 
        result should be in float """
        num :float = (other.dn * self.n) + (self.dn * other.n)
        denom : float= self.dn * other.dn
        #store the value
        Fraction1 = Fraction(num,denom)
        result_plus = Fraction1
        #retuen the value which store the answer
        return result_plus
        # TODO: implement me
        
    def minus(self, other: "Fraction") -> "Fraction":
        """ subtract two fractions using simplest approach 
            Calculate new numerator and denominator and return new Fraction
        """
        """code for the minus when we have value on that which value do which operation with which another value 
        result should be in float"""
        num : float= (other.dn * self.n) - (self.dn * other.n)
        denom : float= self.dn * other.dn
        #store the value
        Fraction1 = Fraction(num,denom)
        result_minus = Fraction1
        #return the answer
        return result_minus
        # TODO: implement me
        
    def times(self, other: "Fraction") -> "Fraction":
        """ Multiply two fractions using simplest approach 
            Calculate new numerator and denominator and return new Fraction
        """
        """code for the times when we have value on that which value do which operation with which another value 
         result should be in float"""
        num : float= self.n * other.n
        denom :float = self.dn * other.dn
        #store the value
        Fraction1 = Fraction(num,denom)
        result_times = Fraction1
        #return the answer
        return result_times
        # TODO: implement me
        
    def divide(self, other: "Fraction") -> "Fraction":
        """ Add two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        """code for the plus when we have value on that which value do which operation with which another value 
         result should be in float"""
        num :float= self.n * other.dn
        denom :float= other.n * self.dn
        #store the value
        Fraction1 = Fraction(num,denom)
        result_divide = Fraction1
        #return asnwer
        return result_divide
        # TODO: implement me
        
    def equal(self, other: "Fraction")-> bool:
        """ return True/False if the two fractions are equivalent """
        # TODO: implement me
        #return the value when same and we want the result in true or false
        if ((self.n == other.n) and (self.dn == other.dn)):
            return True
        else:
            return False



def test_suite() -> None:
    """ We'll see a better testing approach next week but here's a start.
        Note that each statement includes the result of the computation plus 
        the expected answer to help to quickly identify if everything works properly.
    """
    #test case for only two operands
    f34: Fraction = Fraction(3,4)
    f56: Fraction = Fraction(5, 6)
    f78: Fraction = Fraction(7,8)
    f910: Fraction = Fraction(9,10)
    f1011: Fraction = Fraction(10,11)
    f912: Fraction = Fraction(9, 12)
    f128: Fraction = Fraction(3,2)
    f32: Fraction = Fraction(3,2)
    #print each and every result 
    # print(f"{f12} + {f34} = {f12.plus(f34)} [10/8]")
    print(f"{f34} + {f910} = {f34.plus(f910)} [66/40]")
    print(f"{f78} / {f56} = {f78.divide(f56)} [42/40]")
    print(f"{f912} * {f910} = {f912.times(f910)} [81/120]")
    print(f"{f1011} - {f34} = {f1011.minus(f34)} [7/44]")
    print(f"{f128} == {f32} = {f128.equal(f32)}")
    
    # include a test with three operands "+,*,/,-,="
    #print each and every result 
    print(f"{f34} + {f56} + {f78} = {f34.plus(f56).plus(f78)} [472/192]")
    print(f"{f56} * {f912} * {f78} = {f56.times(f912).times(f78)} [315/576]")
    print(f"{f78} - {f56} - {f1011} = {f78.minus(f56).minus(f1011)} [-458/528]")
    print(f"{f912} / {f910} / {f78} = {f912.divide(f910).divide(f78)} [720/756]")
    # TODO: Be sure to test all methods, including __str__
    
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
        """ in franction when denomator is 0 on that it will say it is not valid and ask for another number"""
        if dn == 0:
            print('d cannot be zero')
            dn:float = int(input('enter your denom'))
        """store the value of the operation """
        fraction: Fraction=Fraction(n,dn)
        return fraction

        # TODO: use the same approach as get_number() to retrieve 
        # TODO: an instance of class Fraction
    
def compute(f1: Fraction, operator: str, f2: Fraction) -> None:
    """ Given two fractions and an operator, return the result
        of applying the operator to the two fractions
    """
    result: Fraction
    """define result should be true only"""
    okay: bool = True 
    """condition for the all the operator when we call that and display the result all the value is true"""
    if operator == '+':
        result = f1.plus(f2)
    elif operator == "-":
        result = f1.minus(f2)
    elif operator == "*":
        result = f1.times(f2)
    elif operator == "/":
        result = f1.divide(f2)
    elif operator == "==":
        result = f1.equal(f2)
    else:
        #display the massage when value is wrong
        print(f"Error: '{operator}' is an unrecognized operator")
        okay = False

    if okay:
        print(f"{f1} {operator} {f2} = {result}")

       
def main() -> None:
    """ Fraction calculations """
    print('Welcome to the fraction calculator!')
    f1: Fraction = get_fraction()
    operator: str = input("Operation (+, -, *, /): ")
    f2: Fraction = get_fraction()
    
    try:
        compute(f1, operator, f2)
    except ZeroDivisionError as e:
        print(e)
        
if __name__ == '__main__':
    test_suite()
    main()


