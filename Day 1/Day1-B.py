import fileinput

fname = 'input.txt'

a = []
b = []

for line in fileinput.input(files=fname):
    a.append(int(line[0:5]))
    b.append(int(line[8:13]))

a.sort()
b.sort()

freqScore = 0
for i in range(0, len(a)):
    freqScore += a[i] * b.count(a[i])

print(freqScore)
