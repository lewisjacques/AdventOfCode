import sys
sys.path.insert(0, "..")
from aoc_tools import retrieve_input
import re

class Day0:
    def __init__(self):
        # Retrieve data 
        self.day_num = re.findall(r"Day(\d{1,2})", self.__class__.__name__)[0]
        raw_input = retrieve_input(self.day_num)

        # Parse data according to input format
        self.input_1 = self.parse_input(raw_input)
        self.input_2 = self.parse_input(raw_input, part=2)
        self.raw_input = raw_input

        # Calculate output values
        self.output_p1 = self.calc_result_p1()
        self.output_p2 = self.calc_result_p2()
    
    @staticmethod
    def parse_input(raw_input:str, part=1) -> list:
        """
        Parse input speciic to the formatting of the day

        Args:
            raw_input (str): Raw values from the aoc base url

        Returns:
            :
        """

        return(None)
    
    def calc_result_p1(self) -> int:
        """
        Function with a shared namesake across DayX classes.
        Calculate the first part of the problem

        Returns:
            int: Value provided to aoc
        """

        return(None)
    
    def calc_result_p2(self) -> int:
        """
        Function with a shared namesake across DayX classes.
        Calculate the first part of the problem

        Returns:
            int: Value provided to aoc
        """

        return(None)
    
print(f"Result p1: {Day0().output_p1}")
print(f"Result p2: {Day0().output_p2}")