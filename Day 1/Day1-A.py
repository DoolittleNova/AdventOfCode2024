import fileinput

fname = 'input.txt'

a = []
b = []

for line in fileinput.input(files=fname):
    a.append(int(line[0:5]))
    b.append(int(line[8:13]))

a.sort()
b.sort()

dist = 0
for i in range(0, len(a)):
    dist += abs(a[i] - b[i])

print(dist)
