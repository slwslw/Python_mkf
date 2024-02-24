import itertools as it
f = open('studygroup.txt')
lines = f.readline().split()
for x, y, z in it.combinations(lines, 3):
    print("1:", x, "2:", y, "3:", z, sep=' ')
f.close()
