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
    elf_list = load_file(filename)
    max_elf = elf_list[0]
    for i in range(1, len(elf_list)):
        if elf_list[i] > max_elf:
            max_elf = elf_list[i]
    print('Elf with most calories is carrying:', max_elf )    

if __name__ == '__main__':
    main()