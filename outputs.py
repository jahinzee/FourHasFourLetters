"""
FourHasFourLetters -- A Python app that demonstrates the weird and wonderful world of worded-form-length functions.
Copyright (c) 2022 jahinzee (Jahin Z.)

----

## Outputs

Returning the results in text form

"""

from core_functions import Chain
from tabulate import tabulate
from colorama import init as colorama_init, Fore

class ChainOutput(Chain):

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

    def __init__(self, i, language=None):
        """
        constructor
        @param i:        number to begin chain with
        @param language: language to use
        """
        
        super().__init__(language)

        # initialise colorama
        colorama_init()

        # calculate chain and loop start index
        self.array, loop_start = super().gen(i)

        # create list to store if idx in array is a loop value
        self.idx_is_loop = []

        # populate list with True/False values
        for idx, val in enumerate(self.array):
            self.idx_is_loop.append(idx >= loop_start)

    def __str__(self):
        """
        string representation of ChainOutput
        @return: a string of ints representing the chain
                 - each value is separated by an edge symbol
                 - loop values are highlighted in yellow
        """
        
        out = ""

        for item, is_loop in zip(self.array, self.idx_is_loop):
            
            # highlight item if it is a loop value
            out += self.COLORS["element_loop"] if is_loop else self.COLORS["element"]
            out += str(item)

            # add edge where appropriate
            if (item != self.array[-1]):
                out += self.COLORS["edge"]
                out += self.SYMBOLS["edge"]

            # reset highlight; it's the right thing to do :)
            out += Fore.RESET

        return out