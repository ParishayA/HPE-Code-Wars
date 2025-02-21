import sys

for line in sys.stdin:
    line = line.strip()
    numbers = sorted([c for c in line if c.isdigit()])
    letters = sorted([c for c in line if c.isalpha()])
    
    result = list(line)
    num_index, letter_index = 0, 0
    
    for i in range(len(line)):
        if line[i].isdigit():
            result[i] = numbers[num_index]
            num_index += 1
        elif line[i].isalpha():
            result[i] = letters[letter_index]
            letter_index += 1
    
    print("".join(result))
