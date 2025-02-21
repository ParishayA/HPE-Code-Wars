import sys

num_students = int(sys.stdin.readline().strip())

for _ in range(num_students):
    name, years, months = sys.stdin.readline().split()
    years, months = int(years), int(months)
    total_months = (25 * 12) - (years * 12 + months)
    print(f"{name} {total_months}")
