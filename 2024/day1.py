import sys
sys.path.insert(0, "..")
from aoc_tools import retrieve_input
import re

class Day1:
    def __init__(self):
        # Retrieve data 
        self.day_num = re.findall(r"Day(\d{1,2})", self.__class__.__name__)[0]
        raw_input = retrieve_input(self.day_num)

        # Parse data according to input format
        self.left, self.right = self.parse_input(raw_input)

        # Calculate output values
        self.output_p1 = self.calc_result_p1()
        self.output_p2 = self.calc_result_p2()
    
    @staticmethod
    def parse_input(raw_input:str) -> tuple:
        """
        Parse input speciic to the formatting of the day

        Args:
            raw_input (str): Raw values from the aoc base url

        Returns:
            tuple: left and right columns as lists from the input
        """

        # Complete left list
        full_l = []
        # Complete right list
        full_r = []
        for row in raw_input.split("\n"):
            # Skip empty and final row(s)
            if row == "":
                continue

            vals = row.split("   ")
            assert len(vals) == 2, f"Unexpected input formatting, vals: {vals}"

            full_l.append(int(vals[0]))
            full_r.append(int(vals[1]))

        return(full_l, full_r)
    
    def calc_result_p1(self) -> int:
        """
        Function with a shared namesake across DayX classes.
        Calculate the first part of the problem

        Returns:
            int: Value provided to aoc
        """
        # Order lists
        left_ordered = sorted(self.left)
        right_ordered = sorted(self.right)

        diff_count = 0
        # left and right lists should be the same length
        for ind,l in enumerate(left_ordered):
            diff_count += abs(l-right_ordered[ind])

        return(diff_count)
    
    def calc_result_p2(self) -> int:
        """
        Function with a shared namesake across DayX classes.
        Calculate the second part of the problem

        Returns:
            int: Value provided to aoc
        """

        # Initialise a value for every entry in the left list
        r_val_count = {k:0 for k in set(self.left)}
        for v in self.right:
            if v in self.left:
                r_val_count[v] += 1
            else:
                continue

        sim_score = sum([lv*r_val_count[lv] for lv in self.left])
        return(sim_score)
    
d = Day1()
print(f"Result p1: {d.output_p1}")
print(f"Result p2: {d.output_p2}")