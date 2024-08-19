def pattern_identifier(files_path):
    number_line = {}  # dictionary to store lines number appears
    number_count = {}  # dictionary to store occurrence of number

    with open(file_path , 'r') as file:
        for line_index, line_content in enumerate(file, 1):
            numbers = line_content.strip().split()
            for number in numbers:
                num = int(number)
                # print(num)

                # updating line appearances
                if num not in number_line:
                    number_line[num] = set()
                number_line[num].add(line_index)
                # print(number_line)

                # updating number count
                number_count[num] = number_count.get(num, 0) + 1
    return number_line, number_count


file_path = 'set2.txt'
minsup = 2
listLoop = list()
num_line, num_count = pattern_identifier(file_path)

# Number Occurrence count
print("Number, number count: ", end=" ")
print(num_count, end="\n")

# for number, count in num_count.items():
#     print(num_count)
#     #print(f"{number}:{num_count}", end=" ",)

print("Number, Line appearance")
for num, line_appearance in num_line.items():
    print(f"{num}: {line_appearance}")

# Number Appearances
for number, line_appearances in num_count.items():  # iterating and pruning to minsup
    # print(num_line)
    if num_count[number] >= minsup:
        listLoop.append(number)
    else:
        del num_line[number]
    # print(f"{number}:{line_appearances}", end=",\n")

# sorting looping list
listLoop.sort()
print(f"list loop: {listLoop}")

# newDict = []
# newSet = set()
for x in range(len(listLoop)):
    newSet = set(num_line[listLoop[x]])
    for y in range(x + 1, len(listLoop)):
        # print(listLoop[x], listLoop[y])
        newSet_2 = set(num_line[listLoop[y]])
        # newSet.add(set((num_line[listLoop[x]])))
        #  newSet_2.add(set(num_line[listLoop[y]]))
        key = (listLoop[x], listLoop[y])
        # print(newSet, newSet_2, newSet.intersection(newSet_2))
        s = newSet.intersection(newSet_2)

        results = {key: s}
        # print(s)
        # newListSet = list()
        # newListSet.append([listLoop[x]])
        # newListSet.append([listLoop[y]])
        # print(newListSet, s)
        if len(newSet.intersection(newSet_2)) >= minsup:
            print(results)
            print(num_line[listLoop[x]], num_line[listLoop[y]], newSet.intersection(newSet_2))
            num_line[key] = s

print(num_line)
