def load_file(filename):
    elves = []
    total_cals = 0
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line == '':
                elves.append(total_cals)
                total_cals = 0 
            else:
                cals = int(line)
                total_cals += cals
        elves.append(total_cals)
    return elves            

def main():
    filename = 'Day01/input.txt'
    # filename = 'Day01/test.txt'
    elf_list = load_file(filename)
    max_elf = elf_list[0]
    for i in range(1, len(elf_list)):
        if elf_list[i] > max_elf:
            max_elf = elf_list[i]
    print('Part 1: Elf with most calories is carrying', max_elf, 'calories')  

    # Part 2
    elf_list.sort(reverse=True)
    top_three = 0
    for i in range(3):
        top_three += elf_list[i]
    print('Part 2: Top 3 elves are carrying', top_three, 'calories')

if __name__ == '__main__':
    main()