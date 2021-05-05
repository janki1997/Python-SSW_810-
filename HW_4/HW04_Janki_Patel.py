
"""
@author: Janki patel
CWID : 10457365
"""
"""int this file we will make fuction which count the vowel, define the last occurence word then make enumerate"""

import random
import unittest
from typing import Any, List, Optional, Sequence, Iterator

# PART 1

def count_vowels(s: str) -> int:
    ''' return the number of vowels in the string s '''
    vowel :int = 0
    for i in s.lower():
        """declared the list"""

        l=['a','e','i','o','u']
        """count vowel condition"""
        if i in l:
            vowel+=1
    return vowel
 
# PART 2
    
def last_occurrence(target: Any, seq: Sequence[Any]) -> Optional[int]:
    ''' return the offset from 0 of the last occurrence of target in seq '''
    last_find:int = None
    for i in range(len(seq)):
        if(seq[i] == target):
            last_find = i
    """condition for the checking that in that object has something or not"""
    if(last_find == None):
        return None
    else:
        """return the last_find"""
        return last_find
 
# PART 4
def my_enumerate(seq: Sequence[Any]) -> Iterator[Any]:
    """ this method return offset and i which has zip that is why value and offset in one
    """    
    for v1,v2 in zip(range(len(seq)),seq):
        yield  v1,v2


