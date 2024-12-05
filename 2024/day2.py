import sys
sys.path.insert(0, "..")
from aoc_tools import retrieve_input
from copy import deepcopy

class Report:
    def __init__(self, report_str:str, part2:bool):
        self.report_str = report_str
        self.levels = self.get_levels(report_str)
        safe = self.get_status(self.levels)

        if not safe and part2:
            safe = self.double_check_unsafe_report()
        self.safe = safe

    @staticmethod
    def get_levels(report_str:str) -> list:
        levels = [int(l) for l in report_str.split(" ") if l != ""]
        return(levels)
    
    def set_unsafe_point(self, index:int|None) -> None:
        self.unsafe_point = index

    def get_status(self, levels:list, set_unsafe=True) -> bool:
        for ind, l in enumerate(levels):
            # 1st Level
            if ind == 0:
                cur_pos_delta = None
                p_val = l
                continue
            else:
                diff = l - p_val
                # Initialise pre_pos_delta
                pre_pos_delta = cur_pos_delta
                cur_pos_delta = diff > 0
                p_val = l

                # Second value, only check diff
                if pre_pos_delta is None:
                    if abs(diff) == 0 or abs(diff) > 3:
                        if set_unsafe:
                            self.set_unsafe_point(ind)
                        return(False)
                    continue

                # All requirements for a non-safe report
                if  pre_pos_delta != cur_pos_delta or \
                    abs(diff) == 0 or abs(diff) > 3:
                    if set_unsafe:
                        self.set_unsafe_point(ind)
                    return(False)
                
        if set_unsafe:    
            self.set_unsafe_point(None)
        return(True)
    
    def double_check_unsafe_report(self):
        # Try removing indexes from both problematic values
        for bookends in range(-1,1):
            new_levels = deepcopy(self.levels)
            new_levels.pop(self.unsafe_point+bookends)
            new_status = self.get_status(new_levels, set_unsafe=False)
            # If now safe, return
            if new_status:
                print("Successfully found safe")
                print(f"Old levels {self.levels}")
                print(f"Index removed: {self.unsafe_point+bookends}")
                print(f"New levels: {new_levels}")
                return(True)

            print("Report still Unsafe")
            print(f"Levels {self.levels}")
            print(f"Removed index: {self.unsafe_point+bookends}")
            print(f"New levels: {new_levels}")

        return(new_status)

class Day2:
    def __init__(self, part2=False):
        # Retrieve data 
        self.day_num = re.findall(r"Day(\d{1,2})", self.__class__.__name__)[0]
        raw_input = retrieve_input(self.day_num)
        # Parse data according to input format
        self.reports = self.parse_input(raw_input, part2)
        # Calculate output values
        self.output = self.calc_safe_count()
    
    @staticmethod
    def parse_input(raw_input:str, part2:bool) -> tuple:
        """
        Parse input speciic to the formatting of the day

        Args:
            raw_input (str): Raw values from the aoc base url

        Returns:
            list: Report objects containing 5 levels each
        """
        return([Report(r, part2) for r in raw_input.split("\n") if r != ""])
    
    def calc_safe_count(self):
        safe_count = sum([1 for r in self.reports if r.safe])
        return(safe_count)
    
print(f"Result: {Day2(part2=True).output}")