fin = open('input.txt', 'r')
lines = fin.readlines()
lineLength = len(lines[0]) - 1
numLines = len(lines)
print("lineLength: {}, numLines: {}".format(lineLength, numLines))
idx = 0
ret = 1

for right in [1,3,5,7]:
    indivCount = 0
    idx = 0
    for i, line in enumerate(lines):
        if (line[idx] == '#'):
            indivCount += 1
        idx = (idx + right) % lineLength
    ret *= indivCount
    print(ret)

indivCount = 0
idx = 0
for i, line in enumerate(lines):
    if (i % 2 != 0):
        continue
    if (line[idx] == '#'):
        indivCount += 1
    print("lineDex: {}, charAt: {}, idx:{}".format(i, line[idx], idx))
    idx = (idx + 1) % lineLength
ret *= indivCount

print(ret)
