# HPE Code Wars 2024 Problems

# Problem 10
import sys

try:
    #file = open(r"G:\My Drive\HPE Code Wars 2025\2024 Problems\input10.txt", "r")
    with open('input10.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        if line.strip() != "END":
            signIndex = int(line.find("+"))
            equalIndex = int(line.find("="))
            
            num1 = int(line[0:signIndex])
            num2 = int(line[(signIndex + 1) : equalIndex])
            answer = int(line[(equalIndex + 1) : (len(line) - 1)])
        
            if (num1 + num2 == answer):
                print("CORRECT")
            else:
                print(f"WRONG: {num1}+{num2}={num1 + num2}")
except Exception as e:
    print("Error reading file")
    print(f"The error is {e}")