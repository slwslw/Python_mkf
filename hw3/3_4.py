f = open('input.txt')
lst1 = []
lst2 = []
out = open('output.txt', 'w')
num = int(f.readline())
for i in range(num):
    lst1.append(f.readline().strip())
for i in range(num):
    lst2.append(f.readline().strip())
for x, y in zip(lst1, lst2):
    print(x, y, sep='\t', file=out)
f.close()