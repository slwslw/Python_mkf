f = open('input.txt')
lines = f.readlines()
l1 = filter(lambda s: 'ё' in s, lines)
for i in list(l1):
    print(i[0:-1])
f.close()