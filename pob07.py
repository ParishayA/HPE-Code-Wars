import sys

line = sys.stdin.readline().strip()
line = line[:-1]  # Remove the period at the end
found = False

for i in range(len(line) - 3):
    if line[i] == line[i+1] == line[i+2] == line[i+3] and (i+4 >= len(line) or line[i] != line[i+4]):
        print(line[i], end="")
        found = True

if not found:
    print("No Four of a Kind")
