"""
@author: Janki patel
CWID : 10457365
"""

"""In this file we are going to implement reverse method, substring fuction, second occurence and also reading content from the file"""




from typing import Iterator, IO, Sequence, Any, Optional, List
def reverse(s: str) -> str:
    """when user enter their string on that time it will reverse string using for loop"""
    """first I define one variatble and then after I do for loop where word will save one by one and then It will return"""
    s1: str = ""
    for i in s:
        s1 = i + s1
    return s1


def substring(target: str, s: str) -> int:
    """This fuction will return the substring of the original string when 
       it will not availabe on that time it will return None value"""
    i: int = 0
    for i in range(len(s)):
        if s[i:i+(len(target))] == target:
            return i
    return None


def find_second(target: str, string: str) -> int:
    """This fuction return second occurence of the original string of the target string which we define """

    if target not in string:
        """when target string is not in main string then it will return -1"""
        return -1
    else:
        return string.find(target, string.find(target)+1)


def get_lines(path: str) -> Iterator[str]:
    """This fuction will read line from the file and delte the comment and backslash and join it in to one line"""
    try:
        """defin open the file and save it in to one variable"""
        fp = open(path, encoding="utf8")

    except FileNotFoundError:
        raise FileNotFoundError

    else:
        """take that file which we define"""
        with fp:
            for index in fp:
                index: str = index.rstrip()
                """when in the file line end with \\"""
                while index.endswith("\\"):
                    """read each and every line and save it into one variable index"""
                    index = index[:-1]+fp.readline().strip('\n')
                """when something is start from the # then it will be consider as comment so it will not count """
                index = index.split('#', 1)[0].strip()
                if index:
                    yield index
                else:
                    """it will doing continue"""
                    continue
