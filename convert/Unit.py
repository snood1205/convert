# coding=utf-8
"""
This file provides the abstract class Unit
"""


class Unit:
    """
    This class is an abstract parent class to all unit classes
    """
    def __init__(self, name, abbreviation, value=0):
        """
        This is the constructor for Unit
        :param name: the name to set
        :param abbreviation: the abbreviation to set
        """
        self.name = name
        self.abbreviation = abbreviation
        self.value = value

    def __str__(self):
        return "{0} {1}".format(self.value, self.abbreviation)


