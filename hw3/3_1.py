f = open('input.txt')
lines = f.readline()
for line in lines.split():
    print(line[::-1], end=' ')
f.close()


