# importing defaultdict from the collections library
from collections import defaultdict

# creating two dictionary variables 
number_count = defaultdict(int)
number_of_lines = defaultdict(list)
listloop = list()
minsup = 1

# loading text file as a readable
with open('set2.txt', 'r') as file:
    # Loop over each line in the file, using enumerate to also get the line number
    for i, line in enumerate(file, start=1):
         # Split each line into a list of numbers 
        numbers = list(map(int, line.split()))
        for num in numbers:
            # incrementing the number of count for the appearance
            number_count[num] += 1
            # appending the line the number can be found in the number_of_lines 
            number_of_lines[num].append(i)

# Print the count of appearances for each number that appears at least once
print("Number of appearances")
non_counts = {num: count for num, count in number_count.items() if count > 0}
print(non_counts)

# Print the lines on which each number appears
print('\nLines of appearance')
for num, lines in number_of_lines.items():
    if num in non_counts:
        print(f"{num}: {{{', '.join(map(str, lines))}}}")

# filtering of numbers using the minsup variable 
for i in number_count:
    if number_count[i] >= minsup:
        listloop.append(i)
    else:
        number_of_lines.pop(i)

print("\n")
print(listloop)
listloop.sort()

listlooplen = len(listloop)
patternLength = 0

while listlooplen >= 1:
    patternLength = patternLength + 1

    # swap of list
    swapList = list()

    if patternLength == 1:
        # combining elements in the listloop
        for index in range(len(listloop)):
            for index2 in range(index+1, len(listloop)):
                p1 = set(number_of_lines[listloop[index]])
                p2 = set(number_of_lines[listloop[index2]])
            
                if len(p1 & p2) >= minsup:
                    itemset = set([listloop[index], listloop[index2]])
                    lines = p1 & p2
                    print(itemset)
                    number_of_lines[tuple(itemset)] = lines
                    print(itemset)
                    print(lines)
                    swapList.append(itemset)
    else:
        for index in range(len(listloop)):
            firstSet = listloop[index]
            firstList = list(firstSet)
            
            firstPrefix = set(firstList[0: (patternLength-1)])
            firstLastItem = firstList[-1]

            for index2 in range(index+1, len(listloop)):
                secondSet = listloop[index2]
                secondList = list(secondSet)
                
                secondPrefix = set(secondList[0: (patternLength-1)])
                secondLastItem = secondList[-1]
                
                if firstPrefix == secondPrefix and firstLastItem != secondLastItem:
                    p1 = set(number_of_lines[tuple(firstSet)])
                    p2 = set(number_of_lines[tuple(secondSet)])
                    
                    if len(p1 & p2) >= minsup:
                        itemset = set(firstSet | {secondLastItem})
                        lines = p1 & p2
                        print(itemset)
                        number_of_lines[tuple(itemset)] = lines
                        print(itemset)
                        print(lines)
                        swapList.append(itemset)

    listloop = swapList
    listlooplen = len(listloop)

print(number_of_lines)