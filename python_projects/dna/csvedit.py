import csv
import re
from cs50 import get_string
from sys import argv, exit

if len(argv) != 2:
    print("Usage: python csvedit.py category.csv")
    exit(1)

# Open and store all files and csv in varible
reader = csv.reader(open(argv[1]))
STR_list = next(reader)
STR_Values = []

# Creates dictionary and stores database in it
database = {}
for row in reader:
    key = row[0]
    if key in database:
        pass
    database[key] = row[1:]


print(f"{database}")

# Useful links that helped
# https://stackoverflow.com/questions/61131768/how-to-count-consecutive-substring-in-a-string-in-python-3
# https://stackoverflow.com/questions/14091387/creating-a-dictionary-from-a-csv-file
# https://stackoverflow.com/questions/48692264/how-to-import-csv-column-as-list-in-python
# https://docs.python.org/3/library/csv.html
# https://docs.python.org/3/library/re.html