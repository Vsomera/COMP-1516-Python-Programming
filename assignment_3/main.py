# COMP 1516 - Assignment 3
# Vilmor Somera
# 12/11/2022

from country import Country
import random
import data as d

def main():
    try:
        all_countries = []

        for country in d.countries_and_capitals:
            country_pop = random.randint(1000000, 1000000000)
            all_countries.append([country[0], country[1], country_pop])
        
        # Print Details
        print("Details")
        for item in all_countries:
            country_item = Country(item[0], item[1], item[2])
            Country.print_details(country_item)
        print()

        # Birth
        print("Birth")
        for item in all_countries:
            country_item = Country(item[0], item[1], item[2])
            Country.birth(country_item)
            Country.print_details(country_item)
        print()

        # Death
        print("Death")
        for item in all_countries:
            country_item = Country(item[0], item[1], item[2])
            Country.death(country_item)
            Country.print_details(country_item)
        print()

        # Disaster
        print("Disaster")
        for item in all_countries:
            country_item = Country(item[0], item[1], item[2])
            Country.disaster(country_item)
            Country.print_details(country_item)

    except ValueError:
        print("oops")

if __name__ == "__main__":
    main()