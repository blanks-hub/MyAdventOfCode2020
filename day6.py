with open('day6input') as f:
    groups = f.read().split("\n\n")

# Part One
sum = 0
for group in groups:
    l = list()
    group = group.replace('\n', '')
    count = len(set([c for c in group]))    # by creating a set we eliminate all duplicates. The len of that is our count
    sum += count

print(sum)

# Part Two
sum = 0
for group in groups:
    l = list()
    group = group.split("\n")
    groupset = set(group[0])                # first "groupset" needs to be the set of the first person
    for person in group:
        personset = set([c for c in person])
        groupset = groupset & personset     # now we can use the intersection set operation on the group and person set
    sum += len(groupset)                    # and only questions to which everyone answered "yes" are add to our final
                                            # groupset. Now we can sum up the counts
print(sum)