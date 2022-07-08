import csv
import re
from cs50 import get_string
from sys import argv, exit

if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)

# Open and store all files and csv in varible
reader = csv.reader(open(argv[1]))
STR_list = next(reader)
file = open(argv[2])
SAMPLE_DNA = file.read().replace("\n", " ")
STR_Values = []

# Creates dictionary and stores database in it
database = {}
for row in reader:
    key = row[0]
    if key in database:
        pass
    database[key] = row[1:]

# Check how many times each STR is in current sample and store max in STR_Values list
i = 1
maxcount = 0
for g in range(len(STR_list) - 1):
    if re.findall(rf"(?:{STR_list[i]})+", SAMPLE_DNA):
        STR_Match = re.findall(rf"(?:{STR_list[i]})+", SAMPLE_DNA)
        maxcount = max(STR_Match, key=len)
        maxcount = len(maxcount) / len(STR_list[i])
    STR_Values.append(maxcount)
    i += 1
    maxcount = 0

# Check database against STR_Values list for a match
for x in database:
    match = 0
    c = 0
    for t in database[x]:
        if int(t) == int(STR_Values[c]):
            match += 1
        c += 1
    if match == len(STR_Values):
        print(f"{x}")
        exit(1)

print("No match")

# Useful links that helped 
# https://stackoverflow.com/questions/61131768/how-to-count-consecutive-substring-in-a-string-in-python-3
# https://stackoverflow.com/questions/14091387/creating-a-dictionary-from-a-csv-file
# https://stackoverflow.com/questions/48692264/how-to-import-csv-column-as-list-in-python
# https://docs.python.org/3/library/csv.html
# https://docs.python.org/3/library/re.html