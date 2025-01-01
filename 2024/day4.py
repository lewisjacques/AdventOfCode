import sys
sys.path.insert(0, "..")
from aoc_tools import retrieve_input
import re

class WordSearchMatrix:
    def __init__(self, text:list):
        """
        Word Search Matrix initialisation

        Args:
            text (list): List of rows of characters
        """
        self.text = text
        return

    def find_all_instances(self, word:str, directions:list=None, part=1) -> list:
        """
        Find all instances of 'word' by looking in the directions set out in
        the tuples within directions

        Args:
            word (str): word to search
            directions (list): list of tuples to check from the anchor point
            part (int): problem selection

        Returns:
            list: List of all found instances
        """

        assert directions is not None if part == 1 else True, \
            "Directions must be given in part 1"
        assert part in (1,2), f"Part must be in (1,2). Given: {part}"
        rows = len(self.text)
        cols = len(self.text[0])
        word_len = len(word)
        results = []

        def is_valid(x:int, y:int) -> bool:
            """
            Check value at x,y exists within the matrix

            Args:
                x (int): x
                y (int): y

            Returns:
                bool: True if indexes sit within the matrix
            """
            return(0 <= x < rows and 0 <= y < cols)

        def search_from(x:int, y:int, dx:int, dy:int) -> bool:
            """
            Check if the word exists starting from (x, y) in the (dx, dy) direction.

            Args:
                x (int): anchor index, x
                y (int): anchor index, y
                dx (int): change in x [-1,1]
                dy (int): change in y [-1,1]

            Returns:
                bool: True if word is found from location
            """
            # Look up to the length of the word
            for i in range(word_len):
                nx, ny = x + (i * dx), y + (i * dy)
                if not is_valid(nx, ny) or self.text[nx][ny] != word[i]:
                    return False
            return True
        
        ### --- Searching --- ###
        
        # Traverse each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if part==1:
                    # Check all directions from the current cell
                    for dx, dy in directions:
                        if search_from(r, c, dx, dy):
                            results.append((
                                (r, c), 
                                (r + (word_len - 1) * dx, c + (word_len - 1) * dy))
                            )
                else:
                    # Any two diaganals need to be true
                    down_right = search_from(r, c, 1, 1)
                    up_right = search_from(r+2, c, -1, 1)
                    down_left = search_from(r, c+2, 1, -1)
                    up_left = search_from(r+2, c+2, -1, -1)

                    if sum([
                        down_right,
                        up_right,
                        down_left,
                        up_left
                    ]) == 2:
                        # Just append the top left location
                        results.append(
                            (r, c)
                        )
        return results

class Day4:
    MAGIC_WORD_1 = "XMAS"
    MAGIC_WORD_2 = "MAS"

    def __init__(self):
        # Retrieve data 
        self.day_num = re.findall(r"Day(\d{1,2})", self.__class__.__name__)[0]
        raw_input = retrieve_input(self.day_num)

        # Parse data according to input format
        t = "MMMSXXMASM\n" +\
            "MSAMXMSMSA\n" +\
            "AMXSXMAAMM\n" +\
            "MSAMASMSMX\n" +\
            "XMASAMXAMM\n" +\
            "XXAMMXXAMA\n" +\
            "SMSMSASXSS\n" +\
            "SAXAMASAAA\n" +\
            "MAMMMXMMMM\n" +\
            "MXMXAXMASX\n"

        self.wsm = self.parse_input(raw_input)
        self.raw_input = raw_input

        # Calculate output values
        self.output_p1 = self.calc_result_p1()
        self.output_p2 = self.calc_result_p2()
    
    @staticmethod
    def parse_input(raw_input:str) -> list:
        """
        Parse input speciic to the formatting of the day

        Args:
            raw_input (str): Raw values from the aoc base url

        Returns:
            :
        """
        text_rows = [r for r in raw_input.split("\n") if r != ""]
        wsm = WordSearchMatrix(text_rows)

        return(wsm)
    
    def calc_result_p1(self) -> int:
        """
        Function with a shared namesake across DayX classes.
        Calculate the first part of the problem

        Returns:
            int: Value provided to aoc
        """
        instance_coords = self.wsm.find_all_instances(
            self.MAGIC_WORD_1,
            directions = [
                (0, 1),   # Right
                (0, -1),  # Left
                (1, 0),   # Down
                (-1, 0),  # Up
                (1, 1),   # Down-Right
                (1, -1),  # Down-Left
                (-1, 1),  # Up-Right
                (-1, -1)  # Up-Left
            ]
        )
        return(len(instance_coords))
    
    def calc_result_p2(self) -> int:
        """
        Function with a shared namesake across DayX classes.
        Calculate the first part of the problem

        Returns:
            int: Value provided to aoc
        """
        instance_coords = self.wsm.find_all_instances(
            self.MAGIC_WORD_2,
            part=2
        )
        return(len(instance_coords))
    
d = Day4()
print(f"Result p1: {d.output_p1}")
print(f"Result p2: {d.output_p2}")