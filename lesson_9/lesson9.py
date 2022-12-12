# COMP 1516 - Lesson 9
# Vilmor Somera
# 11/23/22

import re

"""
Re.search -> Returns a match object if there is a match anywhere in the string
Checks if string starts with 'The' AND ends with 'Spain'
"""
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# print(x)

"""
Re.Findall -> Returns a list containning all matches
Returns all matches of of 'i' followed by 't' or 's' in txt
"""
# txt = "this is british columbia"
# matches = re.findall(r"i[ts]", txt)
# print(matches) 

"""
Re.match -> searches and returns the first occurence of the given pattern
If a match was found at the beginning of the string, it returns the first occurence
"""
# txt = "it is british columbia"
# matches = re.match("i[ts]", txt)
# print(matches)


"""
Re.search -> will search the whole string for the regex pattern 
and returns the first occurence
Returs a string of all the matches
"""

# txt = "this is british columbia"
# matches = re.findall("i[ts]", txt)
# print(matches)

"""
Re.Finditer -> retuns an iterator yielding a mtach object of all the occurences 
of the given pattern in the string
"""

# txt = "this is british columbia"
# matches = re.finditer("i[ts]", txt)

# for item in matches:
#     print(item)

