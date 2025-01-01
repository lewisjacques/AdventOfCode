import sys
sys.path.insert(0, "..")
from aoc_tools import retrieve_input
import re
import math
from copy import deepcopy

class Rule:
    def __init__(self, rule_str):
        self.x = rule_str.split("|")[0]
        self.y = rule_str.split("|")[1]
        self.rule = rule_str

class Rules:
    def __init__(self, all_rules_str):
        rules = []
        for rule in all_rules_str.split("\n"):
            rules.append(Rule(rule))
        self.rules=rules

class Update:
    def __init__(self, pages_str):
        self.pages = pages_str.split(",")
    
    def check_rule(self, rule:Rule) -> bool:
        """
        Check whether pages are in appropriate orders
        based on x and y in the given Rule

        Args:
            rule (Rule): Rule object

        Returns:
            bool: Valid rule flag
        """
        try:
            x_ind = self.pages.index(rule.x)
            y_ind = self.pages.index(rule.y)
        except ValueError:
            # x or y not in pages
            return(False)
        
        if x_ind < y_ind:
            return(True)
        else:
            return(False)
        
    def get_relevant_rules(self, rules:list) -> list:
        """
        Get rules where both values exist in pages

        Args:
            rules (list): List of Rule objects

        Returns:
            list: List of rules
        """
        rel_rules = []
        for r in rules:
            if r.x in self.pages and r.y in self.pages:
                rel_rules.append(r)
        return(rel_rules)

class Day5:
    def __init__(self):
        # Retrieve data 
        self.day_num = re.findall(r"Day(\d{1,2})", self.__class__.__name__)[0]
        raw_input = retrieve_input(self.day_num)
        self.raw_input = raw_input

        self.rules_objs, self.update_objs = self.parse_input(self.raw_input)

        # Calculate output values
        self.output_p1 = self.calc_result_p1()
        self.output_p2 = self.calc_result_p2()

    def get_update_objects(self, all_updates_str):
        updates = []
        for update in all_updates_str.split("\n"):
            updates.append(Update(update))
        return(updates)
    
    def parse_input(self, raw_input:str) -> tuple:
        """
        Parse input speciic to the formatting of the day

        Args:
            raw_input (str): Raw values from the aoc base url

        Returns:
            parsed_input: tuple 
        """
        split_input = raw_input.split("\n\n")
        rules_objs = Rules(split_input[0])
        update_objs = self.get_update_objects(split_input[1][:-1])

        return((rules_objs,update_objs))
    
    def find_valid_updates(self) -> list:
        valid_updates = []
        for update in self.update_objs:
            # Default to valid
            valid_update = True
            relevant_rules = update.get_relevant_rules(self.rules_objs.rules)

            for rule in relevant_rules:
                valid_rule = update.check_rule(rule)
                # If at least one invalid rule
                if not valid_rule:
                    # Assign invalid and break for loop
                    valid_update = False
                    break
            
            # If valid_update flag still true add to list
            if valid_update:
                valid_updates.append(update)
    
        return(valid_updates)
    
    def find_invalid_updates(self, update_objs:list=None) -> list:
        """
        Get list of invalid updates and the rule they were found to break

        Args:
            update_objs (list): list of update objects

        Returns:
            list: list of invalid objects
        """

        if update_objs is None:
            cur_update_objs = self.update_objs
        else:
            cur_update_objs = update_objs

        invalid_updates = []
        for update in cur_update_objs:
            relevant_rules = update.get_relevant_rules(self.rules_objs.rules)

            for r in relevant_rules:
                valid_rule = update.check_rule(r)
                # If at least one invalid rule
                if not valid_rule:
                    # Append update and the rule it broke
                    invalid_updates.append((update, r.rule))
                    break
                
        return(invalid_updates)

    def calc_result_p1(self) -> int:
        """
        Function with a shared namesake across DayX classes.
        Calculate the first part of the problem

        Returns:
            int: Value provided to aoc
        """
        valid_updates = self.find_valid_updates()
        mid_num_valid_updates = [int(u.pages[math.floor(len(u.pages)/2)]) for u in valid_updates]
        return(sum(mid_num_valid_updates))
    
    def calc_result_p2(self) -> int:
        """
        Function with a shared namesake across DayX classes.
        Calculate the first part of the problem

        Returns:
            int: Value provided to aoc
        """
        # Get original updates
        invalid_updates = self.find_invalid_updates()
        clean_invalid_updates = []

        for u,r in invalid_updates:
            update_valid = False
            old_pages = deepcopy(u.pages)
            old_rule = deepcopy(r)

            # Keep updating order if invalid
            while not update_valid:                
                r1,r2 = old_rule.split("|")
                # Swap the two indexes for incorrect pages
                old_pages[old_pages.index(r1)], old_pages[old_pages.index(r2)] =\
                    old_pages[old_pages.index(r2)], old_pages[old_pages.index(r1)]
                
                # Check updated pages
                new_update = Update(",".join(old_pages))
                relevant_rules = new_update.get_relevant_rules(self.rules_objs.rules)

                for rule in relevant_rules:
                    valid_rule = new_update.check_rule(rule)

                    if not valid_rule:
                        # rule is invalid
                        old_rule = rule.rule
                        break

                if valid_rule:
                    # All rules are valid
                    clean_invalid_updates.append(new_update)
                    update_valid = True

        # Clean invalid updates
        mid_num_valid_updates = [int(u.pages[math.floor(len(u.pages)/2)]) for u in clean_invalid_updates]
        return(sum(mid_num_valid_updates))
    
d = Day5()
print(f"Result p1: {d.output_p1}")
print(f"Result p2: {d.output_p2}")