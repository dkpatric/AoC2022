def day04part1(filename):
    contained_count = 0
    with open(filename) as file:
        for line in file:
            elves = line.strip().split(',')
            elf1 = elves[0]
            elf2 = elves[1]
            left_elf = elf1.split('-')
            right_elf = elf2.split('-')
            print('left_elf[0]:', left_elf[0])
            print('right_elf[0]:', right_elf[0])
            print('left_elf[1]:', left_elf[1])
            print('right_elf[1]:', right_elf[1])
            if (left_elf[0] <= right_elf[0] and left_elf[1] >= right_elf[1]):
                print('left contains right:', line.strip())
                print('left:', 12 <= 6)
                print('right:', 12 >= 12)
                print('left_elf[0] <= right_elf[0]:', left_elf[0] <= right_elf[0])
                print('left_elf[1] >= right_elf[1]:', left_elf[1] >= right_elf[1])
                contained_count += 1
            elif (left_elf[0] >= right_elf[0] and left_elf[1] <= right_elf[1]):
                print('right contains left:', line.strip())
                print('left_elf[0] >= right_elf[0]:', left_elf[0] >= right_elf[0])
                print('left_elf[1] <= right_elf[1]:', left_elf[1] <= right_elf[1])
                contained_count += 1
    return contained_count

def main():
    # filename = 'Day04/test.txt'
    filename = 'Day04/test1.txt'
    # filename = 'Day04/input.txt'
    contained = day04part1(filename)
    print('contained count:', contained),

if __name__ == '__main__':
    main()