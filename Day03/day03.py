def part01(filename):
    priority_list = seq = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    total = 0
    with open(filename) as file:
        for line in file:
            line = line.strip()
            mid = len(line) // 2
            comp1 = line[:mid]
            comp2 = line[mid:]
            # print('comp1:', comp1)
            # print('comp2:', comp2)
            for i in range(len(comp1)):
                for j in range(len(comp2)):
                    if comp2[j] == comp1[i]:
                        # print('matched on:', comp1[i])
                        target = comp1[i]
                        break
            for i in range(len(priority_list)):
                if priority_list[i] == target:
                    priority = i + 1
                    # print('priority =', priority)
                    total += priority
                    break
    return total

def part02(filename):
    priority_list = seq = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    total = 0
    with open(filename) as file:
        for line in file:
            pack1 = line.strip()
            pack2 = next(file).strip()
            pack3 = next(file).strip()
            set2 = set(pack2)
            set3 = set(pack3)
            for item in pack1:
                if (item in set2) and (item in set3):
                    # print('common item:', item)
                    target = item
                    break
                               
            for i in range(len(priority_list)):
                if priority_list[i] == target:
                    priority = i + 1
                    # print('priority =', priority)
                    total += priority
                    break
    return total

def main():
    # filename = 'Day03/test.txt'
    filename = 'Day03/input.txt'
    print('total =', part02(filename))

if __name__ == '__main__':
    main()