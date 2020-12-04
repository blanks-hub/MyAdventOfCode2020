def treesHit(right, down):
    f = open('day3input')
    forest = [line for line in f]

    tree_ctr = 0
    pos = 0
    for i, biome in enumerate(forest):
        if i % down == 0:
            while pos >= len(biome) - 1:
                biome = biome.strip()
                biome += biome

            if biome[pos] == '#':
                tree_ctr += 1

            pos += right
    return tree_ctr


a = treesHit(1, 1)
b = treesHit(3, 1)
c = treesHit(5, 1)
d = treesHit(7, 1)
e = treesHit(1, 2)
# print(a)
print(a * b * c * d * e)
