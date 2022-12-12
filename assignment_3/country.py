# COMP 1516 - Assignment 3
# Vilmor Somera
# 12/11/2022


class Country:
    def __init__(self, country_name, capital_name, population):
        self.country_name = country_name
        self.capital_name = capital_name
        if population < 2000000: 
            raise ValueError(f"Population {population} is too low")
        else:
            self.pop = population

    
    def print_details(self):
        """
        Method prints formatted data
        """
        print(f"The capital of {self.country_name} (pop. {self.pop}) is {self.capital_name}")

    def birth(self):
        """
        Method adds 1 to the objects own self population
        """
        return self.pop + 1

    def death(self):
        """
        Method subtracts 1 to the objects own self population
        """
        return self.pop - 1

    def disaster(self):
        """
        For countries with a population of 100 million or higher, this method subtracts 100 million 
        from the population for smaller countryes it sets the population to 0
        """
        if self.pop >= 100000000:
            self.pop - 100000000
        else:
            self.pop = 0

        