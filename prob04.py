import sys

separator = sys.stdin.readline().strip()
art_line = sys.stdin.readline().strip()
print("\n".join(art_line.split(separator)))

