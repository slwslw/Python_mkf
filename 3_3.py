f = open('input.txt')
lines = f.readlines()
for line in lines:
    a = line.split()
    for str in a[::2]:
        print(str, end=' ')
    print()
f.close()