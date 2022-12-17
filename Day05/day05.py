import node_stack

stack1 = node_stack.Stack()
stack2 = node_stack.Stack()
stack3 = node_stack.Stack()
stack4 = node_stack.Stack()
stack5 = node_stack.Stack()
stack6 = node_stack.Stack()
stack7 = node_stack.Stack()
stack8 = node_stack.Stack()
stack9 = node_stack.Stack()

def day05testsetup():
    stack1.push('Z')
    stack1.push('N')

    stack2.push('M')
    stack2.push('C')
    stack2.push('D')

    stack3.push('P')

    print('stack1:', stack1)
    print('stack2:', stack2)
    print('stack3:', stack3)

    print('top of stack1:', stack1.peek())
    print('top of stack2:', stack2.peek())
    print('top of stack3:', stack3.peek())

def day05part1test(filename):
    day05testsetup()
    with open(filename) as file:
        for line in file:
            cmd = line.strip()
            if cmd[0:4] == 'move':
                cmds = cmd.split()
                amt = int(cmds[1])
                source = int(cmds[3])
                dest = int(cmds[5])
                print(cmd)
                print('amt:', amt, 'source:', source, 'dest:', dest)
                for i in range(amt):
                    if source == 1:
                        crate = stack1.pop()
                    elif source == 2:
                        crate = stack2.pop()
                    elif source == 3:
                        crate = stack3.pop()
                    else:
                        raise ValueError('Invalid source stack: ' + source)

                    if dest == 1:
                        stack1.push(crate)
                    elif dest == 2:
                        stack2.push(crate)
                    elif dest == 3:
                        stack3.push(crate)
                    else:
                        raise ValueError('Invalid dest stack: ' + dest)

    print(stack1.peek() + stack2.peek() + stack3.peek())

def day05setup():
    group = ['D', 'H', 'N', 'Q', 'T', 'W', 'V', 'B']
    for i in range(len(group)):
        stack1.push(group[i])

    group = ['D', 'W', 'B']
    for i in range(len(group)):
        stack2.push(group[i])

    group = ['T', 'S', 'Q', 'W', 'J', 'C']
    for i in range(len(group)):
        stack3.push(group[i])

    group = ['F', 'J', 'R', 'N', 'Z', 'T', 'P']
    for i in range(len(group)):
        stack4.push(group[i])

    group = ['G', 'P', 'V', 'J', 'M', 'S', 'T']
    for i in range(len(group)):
        stack5.push(group[i])

    group = ['B', 'W', 'F', 'T', 'N']
    for i in range(len(group)):
        stack6.push(group[i])

    group = ['B', 'L', 'D', 'Q', 'F', 'H', 'V', 'N']
    for i in range(len(group)):
        stack7.push(group[i])

    group = ['H', 'P', 'F', 'R']
    for i in range(len(group)):
        stack8.push(group[i])

    group = ['Z', 'S', 'M', 'B', 'L', 'N', 'P', 'H']
    for i in range(len(group)):
        stack9.push(group[i])

    print('stack1:', stack1)
    print('stack2:', stack2)
    print('stack3:', stack3)
    print('stack4:', stack4)
    print('stack5:', stack5)
    print('stack6:', stack6)
    print('stack7:', stack7)
    print('stack8:', stack8)
    print('stack9:', stack9)

    print('top of stack1:', stack1.peek())
    print('top of stack2:', stack2.peek())
    print('top of stack3:', stack3.peek())
    print('top of stack4:', stack4.peek())
    print('top of stack5:', stack5.peek())
    print('top of stack6:', stack6.peek())
    print('top of stack7:', stack7.peek())
    print('top of stack8:', stack8.peek())
    print('top of stack9:', stack9.peek())

def day05part1(filename):
    day05setup()
    with open(filename) as file:
        for line in file:
            cmd = line.strip()
            if cmd[0:4] == 'move':
                cmds = cmd.split()
                amt = int(cmds[1])
                source = int(cmds[3])
                dest = int(cmds[5])
                print(cmd)
                print('amt:', amt, 'source:', source, 'dest:', dest)
                for i in range(amt):
                    if source == 1:
                        crate = stack1.pop()
                    elif source == 2:
                        crate = stack2.pop()
                    elif source == 3:
                        crate = stack3.pop()
                    elif source == 4:
                        crate = stack4.pop()
                    elif source == 5:
                        crate = stack5.pop()
                    elif source == 6:
                        crate = stack6.pop()
                    elif source == 7:
                        crate = stack7.pop()
                    elif source == 8:
                        crate = stack8.pop()
                    elif source == 9:
                        crate = stack9.pop()
                    else:
                        raise ValueError('Invalid source stack: ' + source)

                    if dest == 1:
                        stack1.push(crate)
                    elif dest == 2:
                        stack2.push(crate)
                    elif dest == 3:
                        stack3.push(crate)
                    elif dest == 4:
                        stack4.push(crate)
                    elif dest == 5:
                        stack5.push(crate)
                    elif dest == 6:
                        stack6.push(crate)
                    elif dest == 7:
                        stack7.push(crate)
                    elif dest == 8:
                        stack8.push(crate)
                    elif dest == 9:
                        stack9.push(crate)
                    else:
                        raise ValueError('Invalid dest stack: ' + dest)

    print(stack1.peek() + stack2.peek() + stack3.peek() + \
        stack4.peek() + stack5.peek() + stack6.peek() + \
        stack7.peek() + stack8.peek() + stack9.peek())

def day05part2test(filename):
    day05testsetup()
    crate_stack = node_stack.Stack()
    with open(filename) as file:
        for line in file:
            cmd = line.strip()
            if cmd[0:4] == 'move':
                cmds = cmd.split()
                amt = int(cmds[1])
                source = int(cmds[3])
                dest = int(cmds[5])
                print(cmd)
                print('amt:', amt, 'source:', source, 'dest:', dest)
                if source == 1:
                    for i in range(amt):
                        crate_stack.push(stack1.pop())
                elif source == 2:
                    for i in range(amt):
                        crate_stack.push(stack2.pop())
                elif source == 3:
                    for i in range(amt):
                        crate_stack.push(stack3.pop())
                else:
                    raise ValueError('Invalid source stack: ' + source)

                if dest == 1:
                    for i in range(amt):
                        stack1.push(crate_stack.pop())
                elif dest == 2:
                    for i in range(amt):
                        stack2.push(crate_stack.pop())
                elif dest == 3:
                    for i in range(amt):
                        stack3.push(crate_stack.pop())
                else:
                    raise ValueError('Invalid dest stack: ' + dest)

    print(stack1.peek() + stack2.peek() + stack3.peek())

def day05part2(filename):
    day05setup()
    crate_stack = node_stack.Stack()
    with open(filename) as file:
        for line in file:
            cmd = line.strip()
            if cmd[0:4] == 'move':
                cmds = cmd.split()
                amt = int(cmds[1])
                source = int(cmds[3])
                dest = int(cmds[5])
                print(cmd)
                print('amt:', amt, 'source:', source, 'dest:', dest)
                if source == 1:
                   for i in range(amt):
                         crate_stack.push(stack1.pop())
                elif source == 2:
                    for i in range(amt):
                         crate_stack.push(stack2.pop())
                elif source == 3:
                    for i in range(amt):
                        crate_stack.push(stack3.pop())
                elif source == 4:
                    for i in range(amt):
                        crate_stack.push(stack4.pop())
                elif source == 5:
                    for i in range(amt):
                        crate_stack.push(stack5.pop())
                elif source == 6:
                    for i in range(amt):
                        crate_stack.push(stack6.pop())
                elif source == 7:
                    for i in range(amt):
                        crate_stack.push(stack7.pop())
                elif source == 8:
                    for i in range(amt):
                        crate_stack.push(stack8.pop())
                elif source == 9:
                    for i in range(amt):
                        crate_stack.push(stack9.pop())
                else:
                    raise ValueError('Invalid source stack: ' + source)

                if dest == 1:
                    for i in range(amt):
                        stack1.push(crate_stack.pop())
                elif dest == 2:
                    for i in range(amt):
                        stack2.push(crate_stack.pop())
                elif dest == 3:
                    for i in range(amt):
                        stack3.push(crate_stack.pop())
                elif dest == 4:
                    for i in range(amt):
                        stack4.push(crate_stack.pop())
                elif dest == 5:
                    for i in range(amt):
                        stack5.push(crate_stack.pop())
                elif dest == 6:
                    for i in range(amt):
                        stack6.push(crate_stack.pop())
                elif dest == 7:
                    for i in range(amt):
                        stack7.push(crate_stack.pop())
                elif dest == 8:
                    for i in range(amt):
                        stack8.push(crate_stack.pop())
                elif dest == 9:
                    for i in range(amt):
                        stack9.push(crate_stack.pop())
                else:
                    raise ValueError('Invalid dest stack: ' + dest)

    print(stack1.peek() + stack2.peek() + stack3.peek() + \
        stack4.peek() + stack5.peek() + stack6.peek() + \
        stack7.peek() + stack8.peek() + stack9.peek())


def main():
    # filename = 'Day05/test.txt'
    filename = 'Day05/input.txt'
    day05part2(filename)

if __name__ == '__main__':
    main()