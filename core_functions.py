"""
FourHasFourLetters -- A Python app that demonstrates the weird and wonderful world of worded-form-length functions.
Copyright (c) 2022 jahinzee (Jahin Z.)

----

## Core Functions

Classes defining the Base, Chain, and Reel objects.

"""

from collections import namedtuple
from num2words import num2words

class Base:

    # default language to use if not specified
    DEFAULT_LANGUAGE = 'en'


    def __init__(self, language=None):
        """
        constructor
        @param language: language to use, use default language if not specified
        """

        self._language = language if language is not None else Base.DEFAULT_LANGUAGE
    
    def gen(self, i):
        """
        @param i: number to convert to words
        @return: number of characters in worded i in language
        """

        return len(num2words(i, lang=self._language))
    
class Chain(Base):

    # namedtuple for chains
    Chain = namedtuple('Chain', ('array', 'loop_start_idx'))

    def __init__(self, language=None):
        """
        constructor
        @param language: language to use, use default language if not specified
        """

        super().__init__(language)

    def gen(self, i):
        """
        @param i: number to begin from
        @return:  - a Chain of Base.gen(i), ending when a loop is reached
                  - the starting index of the loop
        """
            
        output = []

        while i not in output:

            output.append(i)
            i = super().gen(i)

        return self.Chain(array=output, loop_start_idx=(len(output) - output[::-1].index(i) - 1))

class Reel(Chain):

    # namedtuple for reels
    Reel = namedtuple('Reel', ('starting_value', 'chain'))

    def __init__(self, language=None):
        """
        constructor
        @param language: language to use, use default language if not specified
        """

        super().__init__(language)
    
    def gen(self, min, max):
        """
        @param min: start of range
        @param max: end of range (inclusive)
        @return:    a list of all chains in the range:
                    - the starting value of the chain
        """
        
        output = []

        for i in range(min, max + 1):
            
            output.append(self.Reel(starting_value=i, chain=super().gen(i)))

        return output

