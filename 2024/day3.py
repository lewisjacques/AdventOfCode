import sys
sys.path.insert(0, "..")
from aoc_tools import retrieve_input
import re

class Day3:
    def __init__(self):
        # Retrieve data 
        self.day_num = re.findall(r"Day(\d{1,2})", self.__class__.__name__)[0]
        raw_input = retrieve_input(self.day_num)

        # Parse data according to input format
        mul_strs_1 = self.parse_input(raw_input)
        mul_strs_2 = self.parse_input(raw_input, part=2)
        self.raw_input = raw_input

        # Calculate output values
        self.output_p1 = self.calc_result(mul_strs_1)
        self.output_p2 = self.calc_result(mul_strs_2)
    
    @staticmethod
    def parse_input(raw_input:str, part=1) -> list:
        """
        Parse input speciic to the formatting of the day

        Args:
            raw_input (str): Raw values from the aoc base url

        Returns:
            tuple: left and right columns as lists from the input
        """
        # Use parse_input to pull all mul()
        re_pattern_1 = r"(mul\(\d{1,3},\d{1,3}\))"

        if part == 1:
            mul_strs = re.findall(re_pattern_1, raw_input)
        else:
            # Part two
            # Get the first section until we hit "don't" number 1
            mul_strs = re.findall(re_pattern_1, raw_input.split("don't()")[0])

            # Match all strings between a do and a don't
            re_pattern_2 = r"do\(\)(.*?)(?=don't\(\))|do\(\)(.*)"
            filtered_strs = re.findall(re_pattern_2, raw_input.replace("\n", ""))
            filtered_strs_list = [b for a in filtered_strs for b in a if b != ""]

            for fs in filtered_strs_list:
                mul_strs = mul_strs + re.findall(re_pattern_1, fs)

        return(mul_strs)
    
    @staticmethod
    def calc_result(mul_strs:list) -> int:
        """
        Function with a shared namesake across DayX classes.
        Calculate the first part of the problem

        Returns:
            int: Value provided to aoc
        """
        sum = 0
        for m in mul_strs:
            vals = re.findall(r"(\d{1,3})", m)
            assert len(vals) == 2, f"Expected 2 values. Received: {vals}"
            
            sum += int(vals[0]) * int(vals[1])
        return(sum)
    
print(f"Result p1: {Day3().output_p1}")
print(f"Result p2: {Day3().output_p2}")