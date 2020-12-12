def main():
    fin = open("input.txt", 'r')
    ret = 0
    for line in fin:
        line = line.strip()

        rule, password = line.split(':')
        rule = rule.strip()
        password = password.strip()

        nums, letter = rule.split(' ')
        num1, num2 = nums.split('-')
        num1, num2 = int(num1), int(num2)
        num1 -= 1
        num2 -= 1

        count = 0
        count += 1 if (password[num1] == letter) else 0
        count += 1 if (password[num2] == letter) else 0

        ret += 1 if (count == 1) else 0
    print(ret)
if __name__ == "__main__":
    main()