import re
# fin = open('input.txt', 'r')
fin = open('new.txt', 'r')
finArray = fin.read().split('\n\n')
refSet = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} # no cid
reqSet = {
    'byr': (1920, 2002),
    'iyr': (2010, 2020),
    'eyr': (2020, 2030),
    'hgtcm': (150, 193),
    'hgtin': (59, 76),
    'hcl': "#[0-9a-f]{6}",
    'ecl': ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    'pid': "[0-9]{9}"
}
print('!!!!!START!!!!!')
# print(set(re.sub(":\S+", "", finArray[0].replace("\n", " ")).split(" ")))
ret = 0

for idx, line in enumerate(finArray):
    line = line.strip()
    attrList = (line.replace("\n", " ")).split(" ")
    currList = set([]) 
    for i in range(len(attrList)):
        attr, val = attrList[i].split(":")
        if (attr == 'byr' and len(val) == 4 and int(val) >= reqSet['byr'][0] and int(val) <= reqSet['byr'][1]):
            currList.add('byr')
        elif (attr == 'iyr' and len(val) == 4 and int(val) >= reqSet['iyr'][0] and int(val) <= reqSet['iyr'][1]):
            currList.add('iyr')
        elif (attr == 'eyr' and len(val) == 4 and int(val) >= reqSet['eyr'][0] and int(val) <= reqSet['eyr'][1]):
            currList.add('eyr')
        elif (attr == "hgt"):
            if ('cm' in val):
                curr = val.replace('cm','')
                curr = int(curr)
                if (curr >= reqSet['hgtcm'][0] and curr <= reqSet['hgtcm'][1]):
                    currList.add('hgt')
            elif ('in' in val):
                curr = val.replace('in','')
                curr = int(curr)
                if (curr >= reqSet['hgtin'][0] and curr <= reqSet['hgtin'][1]):
                    currList.add('hgt')
        elif (attr == "hcl" and not (re.search(reqSet['hcl'], val) is None)):
            currList.add('hcl')
        elif (attr == "ecl" and val in reqSet['ecl']):
            currList.add('ecl')
        elif (attr == "pid" and not (re.search(reqSet['pid'], val) is None)):
            currList.add('pid')
    print("index: {}, list: {}".format(idx, currList))
    if 'cid' in currList:
        currSet.remove('cid')
    if currList == refSet:
        ret += 1
print(ret)