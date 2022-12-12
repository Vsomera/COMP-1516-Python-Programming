import re
re.split('; |, ',str)

a='Beautiful, is; better*than\nugly'
re.split('; |, |\*|\n',a)
['Beautiful', 'is', 'better', 'than', 'ugly']


