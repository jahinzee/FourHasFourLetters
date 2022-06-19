"""
FourHasFourLetters -- A Python app that demonstrates the weird and wonderful world of worded-form-length functions.
Copyright (c) 2022 jahinzee (Jahin Z.)

----

## Outputs

Returning the results in text form

"""

from core_functions import Chain, Reel
from tabulate import tabulate
from colorama import init as colorama_init, Fore

class ChainOutput():

    # constant: colorama colours for output
    COLORS = {
        "element": Fore.LIGHTWHITE_EX,
        "element_loop": Fore.LIGHTYELLOW_EX,
        "edge": Fore.LIGHTBLACK_EX,
    }

    # constant: symbols for output
    SYMBOLS = {
        "edge": " ━ "
    }

    def __init__(self, chain: Chain.Chain):
        """
        constructor
        @param chain: Chain to output

        OUT:
        a string of ints representing the chain
        - each value is separated by an edge symbol
        - loop values are highlighted in yellow
        """

        # initialise colorama
        colorama_init()

        self.out = ""

        # calculate chain and loop start index
        array, loop_start = chain

        # create list to store if idx in array is a loop value
        self.idx_is_loop = []

        for idx, item in enumerate(array):
            
            # add item
            self.out += self.COLORS["element_loop"] if idx >= loop_start else self.COLORS["element"]
            self.out += str(item)

            # add edge symbol if not last item
            self.out += self.COLORS["edge"] + self.SYMBOLS["edge"] if idx != len(array) - 1 else ""

            # reset highlight; it's the right thing to do :)
            self.out += Fore.RESET

    def __str__(self):
        """
        string representation of ChainOutput
        @return: out
        """
        
        return self.out

class ReelOutput():

    # constant: colorama colours for output
    COLORS = {
        "separator": Fore.LIGHTBLACK_EX
    }

    # constant: symbols for output
    SYMBOLS = {
        "separator": "┆"
    }

    # constant: table styles for tabulate
    TABLE_STYLE = "plain"

    # constant: custom middle separator for tabulate
    MIDDLE_SEPARATOR = True

    def __init__(self, reel: Reel.Reel):
        """
        constructor
        @param reel: Reel to output
        """

        # initialise colorama
        colorama_init()

        # prepare table
        self.array = [["Index", self.COLORS["separator"] + self.SYMBOLS["separator"] + Fore.RESET, "Chain"]]

        # calculate chain and loop start index
        for item in reel:
            self.array.append([item.starting_value, self.COLORS["separator"] + self.SYMBOLS["separator"] + Fore.RESET, ChainOutput(item.chain)])

        # remove middle column if MIDDLE_SEPARATOR is False
        if not self.MIDDLE_SEPARATOR:
            for col in self.array:
                col.pop(1)
        
        # use tabulate to format table
        self.out = tabulate(self.array, tablefmt=self.TABLE_STYLE, headers="firstrow")

    def __str__(self):
        """
        string representation of ReelOutput
        @return: out
        """

        return self.out

if __name__ == "__main__":

    # test reelOutput 1 - 100
    reel = ReelOutput(Reel("fr").gen(1, 100))
    print(reel)
