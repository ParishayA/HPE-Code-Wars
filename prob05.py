import sys

for line in sys.stdin:
    numbers = map(int, line.strip().split())
    print("".join(chr(n) for n in numbers))
