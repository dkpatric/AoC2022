import node_stack

def day05part1setup():
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
    stack1 = node_stack.Stack()
    stack1.push('Z')
    stack1.push('N')

    stack2 = node_stack.Stack()
    stack2.push('M')
    stack2.push('C')
    stack2.push('D')

    stack3 = node_stack.Stack()
    stack3.push('P')

    print('stack1:', stack1)
    print('stack2:', stack2)
    print('stack3:', stack3)

    print('top of stack1:', stack1.peek())
    print('top of stack2:', stack2.peek())
    print('top of stack3:', stack3.peek())

def day05part1(filename):
    day05part1setup()
    with open(filename) as file:
        for line in file:
            cmd = line.strip()
            if cmd[0:4] == 'move':
                print(cmd)

def main():
    filename = 'Day05/test.txt'
    day05part1(filename)

if __name__ == '__main__':
    main()