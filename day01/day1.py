from functools import reduce

def twoSum(arr, target, i, j):
	# 2sum code
	while not (i + j == target) and (i < j):
		sum = arr[i] + arr[j]
		if (sum > target):
			j -= 1
		elif (sum < target):
			i += 1
		else:
			break
	if (arr[i] + arr[j] == target):
		return (i,j)
	else:
		return None

entries = []
fileName = "./input.txt"
file = open(fileName, 'r')

for line in file:
	line.strip()
	entries.append(int(line))

file.close()

entries.sort()
idxRes = []

print(len(entries))
for idx, entry in enumerate(entries):
	target = 2020 - entry
	twoSumRes = twoSum(entries, target, idx + 1, len(entries) - 1)
	if (twoSumRes):
		idxRes.append(twoSumRes[0])
		idxRes.append(twoSumRes[1])
		idxRes.append(idx)
		break

results = [entries[idx] for idx in idxRes]
print("sum: {}".format(sum(results)))
print("mult: {}".format(reduce(lambda a, b: a * b, results)))
# 2sum code
# while not (i + j == 2020) and (i < j):
# 	sum = entries[i] + entries[j]
# 	if (sum > 2020):
# 		j -= 1
# 	elif (sum < 2020):
# 		i += 1
# 	else:
# 		break

# print("entries[i]: {}, entries[j]: {}".format(entries[i], entries[j]))
# print("sum: {}".format(entries[i] + entries[j]))
# print("mult: {}".format(entries[i] * entries[j]))




