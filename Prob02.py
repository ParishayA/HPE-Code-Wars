with open("input.txt", "r") as file:
    x, y = map(int, file.readline().split())

result = x // y * (y + y)  # Using integer division (//) since no decimals are needed

print(result)
