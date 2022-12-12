# COMP 1516 - Lab 11
# Vilmor Somera
# 12/09/22

class Car:
    """
    Represents a car in a car lot
    """
    def __init__(self, make, model, year, cost, price_usd):
        """
        Initializes the car details
        """
        self._make = make
        self._model = model
        self._year = year
        self._cost_usd = cost
        self._price_usd = price_usd
    
    def calc_profit_usd(self):
        """
        Returns the projected profit in usd
        """
        return self._price_usd - self._cost_usd

    def get_details(self):
        """
        Returns a formatted string with the car details
        """
        return f"{self._make} {self._model} for sale for ${self._price_usd} USD"

    def reduce_price(self, reduction):
        """
        Reduces the price value (self._price_usd) by the reduction amount
        """
        return self._price_usd - reduction
