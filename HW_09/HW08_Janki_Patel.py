
"""
@author: Janki patel
CWID : 10457365
"""


"""This .py file we will do  the Date arithmetic, file reader and file analyzer. """

"""This is importing some of the in-built functions"""




from prettytable import PrettyTable
from collections import defaultdict
import os
from datetime import datetime, timedelta
from typing import Iterator, Tuple, Dict, List , IO
def date_arithmetic() -> Tuple[datetime, datetime, int]:
    """ in that data arithmetic  which is diplay the after 3 days of the date """
    day1: datetime = datetime(2020, 2, 27)
    day2: datetime = datetime(2019, 2, 27)
    day3: datetime = datetime(2019, 9, 30)
    day4: datetime = datetime(2019, 2, 1)
    threedaysafter02272000: datetime = day1 + timedelta(days=3)
    threedaysafter02272017: datetime = day2 + timedelta(days=3)
    days_pass01012017_10312017: int = (day3 - day4).days

    return threedaysafter02272000, threedaysafter02272017, days_pass01012017_10312017


def file_reader(path: str, fields: int, sep: str = ",", header: bool = False) -> Iterator[Tuple[str]]:
    """in this method we will do separat all the items in which we gave file in the file path"""
    try:
        file_open: IO = open(path, "r", encoding="utf=8")
        if not (file := file_open):
            raise FileNotFoundError
        """this will do when we open the file after that we will close that"""
        with file:
            for line_n, line in enumerate(file, 1):
                r_line: List[str] = line.rstrip("\n").split(sep)
                r_linecount: int = len(r_line)

                if r_linecount != fields:
                    raise ValueError(
                        f"The file path is {path} have {r_linecount} on line {line_n} but expected {fields}")

                if not header:
                    yield tuple(r_line)
                elif line_n != 1:
                    yield tuple(r_line)
    except FileNotFoundError:
        print(f"path of {path} could not able to find it try it again!!!")


class FileAnalyzer:
    """in this method we will count the how many type attributes occure in the file folder which we define  """

    def __init__(self, directory: str) -> None:
        """it is use for if directory finded or not also initialize directory and analyze that one"""
        if not os.path.exists(directory):
            raise FileNotFoundError(
                f"directory ‘{directory}’ is could not able to found")

        self.directory: str = directory
        self.files_summary: Dict[str, Dict[str, int]] = dict()
        """this will do summerize files"""
        self.analyze_files()

    def analyze_files(self) -> None:
        """when file is find in dire ctory and counting class , method and line ,char,in the .py files which we define it"""
        for file in os.listdir(self.directory):
            if file.endswith(".py"):
                try:
                    if not (fp := open(os.path.join(self.directory, file), "r")):
                        raise FileNotFoundError(
                            f"File {fp} is could not able to found ")

                except FileNotFoundError:
                    print(f"File {fp} could not able to found")

                with fp:
                    class_count: int = 0
                    function_count: int = 0
                    line_count: int = 0
                    char_count: int = 0

                    for line in fp:
                        if line.strip().startswith("def "):
                            function_count = function_count + 1

                        elif line.strip().startswith("class "):
                            class_count = class_count + 1

                        line_count = line_count + 1
                        char_count += len(line)

                    self.files_summary[str(os.path.join(self.directory, file))] = {
                        "class": class_count,
                        "line": line_count,
                        "function": function_count,
                        "char": char_count
                    }

    def pretty_print(self) -> None:
        """this method will do prettytable of file name ,class , methods , lines and charr"""
        table_contain: PrettyTable = PrettyTable()
        table_contain.field_names = [
            "File Name", "Classes", "Functions", "Lines", "Characters"]
        for i, j in self.files_summary.items():

            table_contain.add_row(
                [[i] + j['classes'], j['functions'], j['lines'], j['characters']])
        return table_contain
