import re


def findDates(text):
    regex = r'\b((?:\d{1,2})[-/](?:\d{1,2})[-/](?:\d{2,4})|(?:\d{4})[-/](?:\d{1,2})[-/](?:\d{1,2})|(?:[A-Z][a-z]+) (?:\d{2}), (?:\d{4})|(?:\d{2}) (?:[A-Z][a-z]+), (?:\d{4}))'

    matches = re.findall(regex, text)
    return matches


test_text = """
Today is May 14, 2020, and tomorrow will be 14 May, 2020. 
We also saw dates like 05/14/20, 5/2/2020, 2020/05/14, and 05-14-2020.
Some more dates: 1/1/99, 02/03/1999, and 1999/12/01.
"""
found_dates = findDates(test_text)
print(found_dates)
