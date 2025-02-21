import sys

def remove_repeats(word):
    result = [word[0]]
    for i in range(1, len(word)):
        if word[i] != word[i-1]:
            result.append(word[i])
    return "".join(result)

for line in sys.stdin:
    line = line.strip()
    if line == "STOP":
        break
    words = line.split()
    cleaned = " ".join(remove_repeats(word) for word in words)
    print(cleaned)
