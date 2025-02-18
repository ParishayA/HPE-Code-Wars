# Problem 17

import re
deb = False

def clean_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        numOfCategories = int(lines[0].strip())
        
        for j in range(numOfCategories):
            category1Line = lines[(j+1)].strip()
            equalsIndex = category1Line.index("=")
            category1 = category1Line[0:equalsIndex]
            category1List = category1Line[(equalsIndex+1):len(category1Line)].split(",")
            print(f'{category1List}')
            madLib = lines[(numOfCategories)+1:(len(lines)-1)]
            madLib1 = []
            n_counter = 0
            for category in category1List:
                print(category1,category)
                for line in madLib:
                    #line = line.split(" ")
                    # #print(line)
                    # for i in range (len(line)):
                    #     #print(word)
                    #     if ((line[i] == ("<" + category1.upper() + ">")) or (line[i] == ("<" + category1.upper() + ">,")) or (line[i] == ("<" + category1.upper() + ">."))):
                    #         if deb: print('match')
                    #         line[i] = category1List[n_counter]
                    #         n_counter +=1
                    # if deb: print(line)
                    # madLib1.append(' '.join(line))
                    # if deb: print(madLib1)
                #print(numOfCategories)
                #print(category1Line)
                    print(line)
                    match = re.search(category1,line,re.IGNORECASE)
                    if match:
                        line[match.start(),len(category)]= category
                        print(line)
            print(madLib)

clean_data('input17.txt')