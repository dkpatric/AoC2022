def day04part1(filename):
    contained_count = 0
    with open(filename) as file:
        for line in file:
            elves = line.strip().split(',')
            elf1 = elves[0]
            elf2 = elves[1]
            left_elf = elf1.split('-')
            elflb = int(left_elf[0])
            elfle = int(left_elf[1])
            right_elf = elf2.split('-')
            elfrb = int(right_elf[0])
            elfre = int(right_elf[1])
            if (elflb <= elfrb) and (elfle >= elfre):
                contained_count += 1
            elif (elflb >= elfrb) and (elfle <= elfre):
                contained_count += 1
    return contained_count

def day04part2(filename):
    overlap_count = 0
    with open(filename) as file:
        for line in file:
            elves = line.strip().split(',')
            elf1 = elves[0]
            elf2 = elves[1]
            left_elf = elf1.split('-')
            elflb = int(left_elf[0])
            elfle = int(left_elf[1])
            right_elf = elf2.split('-')
            elfrb = int(right_elf[0])
            elfre = int(right_elf[1])
            if (elflb <= elfrb) and (elfrb <= elfle):
                overlap_count += 1
            elif (elflb <= elfre) and (elfre <= elfle):
                overlap_count += 1
            elif (elfrb <= elflb) and (elflb <= elfre):
                overlap_count += 1
            elif (elfrb <= elfle) and (elfle <= elfre):
                overlap_count += 1
    return overlap_count

def main():
    # filename = 'Day04/test.txt'
    # filename = 'Day04/test1.txt'
    filename = 'Day04/input.txt'
    # contained = day04part1(filename)
    # print('contained count:', contained),
    overlap = day04part2(filename)
    print('overlap count:', overlap)

if __name__ == '__main__':
    main()