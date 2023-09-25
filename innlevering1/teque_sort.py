from collections import deque


def main():
    n = int(input().strip())
    frontDeque = deque()
    backDeque = deque()

    for _ in range(n):
        command_line = input().strip().split()
        command, x = command_line[0], int(command_line[1])

        if command == 'push_back':
            backDeque.append(x)
            if len(backDeque) > len(frontDeque) + 1:
                frontDeque.append(backDeque.popleft())

        elif command == 'push_front':
            frontDeque.appendleft(x)
            if len(frontDeque) > len(backDeque):
                backDeque.appendleft(frontDeque.pop())

        elif command == 'push_middle':
            if len(frontDeque) == len(backDeque):
                frontDeque.append(x)
            elif len(frontDeque) > len(backDeque):
                backDeque.appendleft(frontDeque.pop())
                frontDeque.append(x)
            else:
                backDeque.appendleft(x)

        elif command == 'get':
            if x < len(frontDeque):
                print(frontDeque[x])
            else:
                print(backDeque[x - len(frontDeque)])


if __name__ == '__main__':
    main()
