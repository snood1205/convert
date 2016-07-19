# coding=utf-8
import convert as cvt
import abc

"""
This file has the abstract class Temperature and its subclasses.
"""


class Temperature(cvt.Unit):
    """
    This class is an abstract parent class to the direct known temperature subclasses:
        - Kelvin
        - Celsius
        - Fahrenheit
    Each subclass must implement the abstract methods.
    """

    def __init__(self, temperature, name="", abbreviation=""):
        """
        This is the constructor for Temperature
        :param temperature: the temperature to set
        """
        super(self.__class__, self).__init__(name, abbreviation, temperature)

    @abc.abstractmethod
    def to_k(self):
        """
        This abstract method converts a temperature to kelvin
        :return: the temperature in kelvins
        """
        pass

    @abc.abstractmethod
    def to_c(self):
        """
        This abstract method converts a temperature to celsius.
        :return: the temperature in degrees celsius.
        """
        pass

    @abc.abstractmethod
    def to_f(self):
        """
        This abstract method converts a temperature to fahrenheit.
        :return: the temperature in degrees fahrenheit
        """
        pass


class Kelvin(Temperature):
    """
    The class Kelvin is a subclass of Temperature. It is the class for temperatures
    expressed in Kelvins.
    """

    def __init__(self, temperature):
        """
        This is the constructor for Kelvin
        :param temperature: the temperature to set
        """
        super(self.__class__, self).__init__(temperature, "Kelvin", "K")

    def to_k(self):
        """
        This overrides the abstract method specified in Temperature
        :return:
        """
        return self

    def to_c(self):
        return Celsius(self.temperature + 273.15)

    def to_f(self):
        return self.to_c().to_f()


class Celsius(Temperature):
    def __init__(self, temperature):
        super(self.__class__, self).__init__(temperature, "Celsius", "C")

    def to_k(self):
        return Kelvin(self.temperature - 273.15)

    def to_c(self):
        return self

    def to_f(self):
        return Fahrenheit(self.temperature * 1.8 + 32)


class Fahrenheit(Temperature):
    def __init__(self, temperature):
        super(self.__class__, self).__init__(temperature, "Fahrenheit", "F")

    def to_k(self):
        return self.to_c().to_k()

    def to_c(self):
        return Celsius((self.temperature - 32) / 1.8)

    def to_f(self):
        return self
