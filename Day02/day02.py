def process_file_part1(filename):
    score = 0
    with open(filename) as file:
        for line in file:
            plays = line.split()
            opponent = plays[0]
            response = plays[1]
            string = 'Opponent: ' + opponent + ' - Response: ' + response
            print(string)
            if opponent == 'A':
                if response == 'X':
                    score += 4  # 1 for rock, 3 for draw
                elif response == 'Y':
                    score += 8  # 2 for paper, 6 for win 
                else:
                    score += 3  # 3 for scissors, 0 for loss
            elif opponent == 'B':
                if response  == 'X':
                    score += 1  # 1 for rock, 0 for loss
                elif response == 'Y':
                    score += 5  # 2 for paper, 3 for draw
                else:
                    score += 9 # 3 for scissors, 6 for win
            else: # opponent == 'C'
                if response == 'X':
                    score += 7  # 1 for rock, 6 for win
                elif response == 'Y':
                    score += 2  # 2 for paper, 0 for loss
                else:
                    score += 6  # 3 for scissors, 3 for draw
    return score
                
def process_file_part2(filename):
    score = 0
    with open(filename) as file:
        for line in file:
            plays = line.split()
            opponent = plays[0]
            response = plays[1]
            string = 'Opponent: ' + opponent + ' - Response: ' + response
            print(string)
            if opponent == 'A':
                if response == 'X':
                    score += 3  # 3 for scissors, 0 for loss
                elif response == 'Y':
                    score += 4  # 1 for rock, 3 for draw 
                else:
                    score += 8  # 2 for paper, 6 for win
            elif opponent == 'B':
                if response  == 'X':
                    score += 1 # 1 for rock, 0 for loss
                elif response == 'Y':
                    score += 5  # 2 for paper, 3 for draw
                else:
                    score += 9  # 3 for scissors, 6 for win
            else: # opponent == 'C'
                if response == 'X':
                    score += 2  # 2 for paper, 0 for loss
                elif response == 'Y':
                    score += 6  # 3 for scissors, 3 for draw
                else:
                    score += 7  # 1 for rock, 6 for win
    return score
                
def main():
    # filename = 'Day02/test.txt'
    filename = 'Day02/input.txt'
    print('Score:', process_file_part2(filename))

if __name__ == '__main__':
    main()