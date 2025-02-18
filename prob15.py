# Problem 15

import re

def format_chemical_formula(line):
    formula = re.match(r'\S+', line).group()
    
    letters = re.sub(r'\d', ' ', formula)
    numbers = re.sub(r'\D', ' ', formula)
    
    return f"{letters}\n{numbers}"

with open('input15.txt', 'r') as file:
    line = file.readline().strip()

print(format_chemical_formula(line))