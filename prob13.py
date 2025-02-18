# Problem 13

try:
    with open('input13.txt', 'r') as file:
        fixedShape = []
        lines = file.readlines()
        
        if not lines:
            raise ValueError("File is empty")
        
        width = len(lines[0].strip())  
        length = len(lines)  
        changed = False
                
        for i in range(len(lines)):
            line = lines[i].rstrip() 
            line = list(line)  
            
            if len(line) < width: 
                line.extend([' '] * (width - len(line) - 1))
                line.append('#')
                changed = True
            
            fixedShape.append("".join(line) + "\n") 
        
        for i in range(width):
            if fixedShape[-1][i] != '#':
                fixedShape[-1] = "#" * width + "\n"
                changed = True
                break
        
        if changed:
            with open('input13_fixed.txt', 'w') as outfile:
                outfile.writelines(fixedShape)
            print("File corrected, saved as 'input13_fixed.txt'")
        else:
            print("Nothing to do")

except Exception as e:
    print("Error reading file")
    print(f"The error is {e}")