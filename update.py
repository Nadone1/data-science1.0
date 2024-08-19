# importing defaultdict frrom the collection library
from collections import defaultdict

# creating two dictionary variables 
number_count = defaultdict(int)
number_of_lines = defaultdict(list)
listloop = list()
minsup = 2

# loadindg text file  as a readable
with open('set2.txt', 'r') as file:
    # Loop over each line in the file, using enumerate to also get the line number
    for i, line in enumerate(file, start=1):
         # Split each line into a list of numbers 
        numbers = list(map(int, line.split()))
        for num in numbers:
            # incremeting the number of count for the appearance the
            number_count[num] += 1
            #appending the line the number can be found in the number_of_lines 
            number_of_lines[num].append(i)


#Print the count of appearances for each number that appears at least once
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
    if(number_count[i]>= minsup):
        listloop.append(i)
    else:
        number_of_lines.pop(i)

print("\n")
print(listloop)
listloop.sort()


listlooplen = len(listloop)
patternLenght = 0

while listlooplen >= 1:
    patternLenght = patternLenght+1

    # swap of list
    swapList = list()

    if patternLenght == 1:
        #combining elements in the listloop
        for index in range(len(listloop)):
            for index2 in range(index+1,len(listloop)):

                p1= set(number_of_lines[listloop[index]])
                p2= set(number_of_lines[listloop[index2]])

            #print(p1)
            #print(p2)
            #print(p1,p2,p1&p2)
            #setLength = len(p1&p2)
            
                if( len(p1&p2) >= minsup):
                    itemset = set()
                    itemset.add(listloop[index])
                    itemset.add(listloop[index2])
                    lines = (p1&p2)
                    print(itemset)
                    number_of_lines[tuple(itemset)]=lines
                    print(itemset)
                    print(lines)
    else:
        for index in range(len(listloop)):
            for index2 in range(index+1,len(listloop)):

                p1= set(number_of_lines[listloop[index]])
                p2= set(number_of_lines[listloop[index2]])

            #print(p1)
            #print(p2)
            #print(p1,p2,p1&p2)
            #setLength = len(p1&p2)
            
                if( len(p1&p2) >= minsup):
                    itemset = set()
                    itemset.add(listloop[index])
                    itemset.add(listloop[index2])
                    lines = (p1&p2)
                    print(itemset)
                    number_of_lines[tuple(itemset)]=lines
                    print(itemset)
                    print(lines)
        #print("(",listloop[index],",",listloop[index2],")")

print(number_of_lines)