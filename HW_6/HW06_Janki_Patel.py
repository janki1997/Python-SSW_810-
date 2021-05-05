"""
@author: Janki patel
CWID : 10457365
"""


"""This  file is we are going to implementing  the copying the list, intersecting the two lists, difference of two lists, removing of the vowels, password checking and 
dounetqueue using list comprehension. """




from typing import Iterator, IO, Sequence, Any, Optional, List
def list_copy(l: List[Any]) -> List[Any]:
    """this fucntion do Copy the list"""
    l1: List[Any] = [value for value in l]
    return l1


def list_intersect(l1: List[Any], l2: List[Any]) -> List[Any]:
    """in this fuction we are taking two string and check the common element of the list and return that element"""
    l1: List[Any] = [value for value in l1 if value in l2]
    return l1


def list_difference(l1: List[Any], l2: List[Any]) -> List[Any]:
    """in this fuction we are taking two string and check the difference element of the list and return that element of the first list"""
    l1: List[Any] = [value for value in l1 if value not in l2]
    return l1


def remove_vowels(s: str) -> str:
    """Remove the elements which starting with vowels int the string"""
    l1: str = " ".join([i for i in s.split(
        " ") if not i.lower().startswith(('a', 'e', 'i', 'o', 'u'))])
    return l1


def check_pwd(password: str) -> bool:
    """the password should be start with digit, atleast two uppercase and atleast one lower case then only password is correct otherwise it will incorrect """
    pw = (len(password) >= 4) and ((len([x for x in password if x.isupper()]) >= 2) and any(
        x.islower() for x in password) and (password[0].isdigit()))
    return pw


class Queue:
    def __init__(self) -> None:
        """difine queue"""
        self.queue: List[str] = list()

    def addcustomer(self, name: str) -> None:
        """All customers in a list which are their"""
        self.queue.append(name)

    def get_nextcustomer(self) -> Optional[str]:
        """find the next customer in line and served it"""
        if len(self.queue) < 1:
            return None
        else:
            return self.queue.pop(0)

    def waitingcustomer(self) -> List[str]:
        """it waiting for customer"""
        return self.queue


class Donutqueue():
    """This class will serve vip customers first and then normal"""

    def __init__(self) -> None:
        """defin vip customer"""
        self.vip_queue: Queue = Queue()
        self.standard_queue: Queue = Queue()

    def arrive(self, name: str, vip: bool) -> None:
        """it define order is arriving"""
        if vip:
            self.vip_queue.addcustomer(name)
        else:
            self.standard_queue.addcustomer(name)

    def next_customer(self) -> str:
        """this fuction decides which customer should be be served next"""
        customer = self.vip_queue.get_nextcustomer()
        if customer is None:
            customer = self.standard_queue.get_nextcustomer()
        return customer

    def waitinglist(self) -> str:
        """waiting list for the  waitingcustomer"""
        vippeople = self.vip_queue.waitingcustomer()
        standardpeople = self.standard_queue.waitingcustomer()
        everyone = vippeople + standardpeople
        """separeted by comma """
        return ", ".join(everyone)
