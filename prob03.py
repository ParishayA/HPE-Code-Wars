import sys

for line in sys.stdin:
    n = int(line.strip())
    if n == -1:
        break
    unit = "minute" if n == 1 else "minutes"
    print(f"You, {n} {unit} ago.")
