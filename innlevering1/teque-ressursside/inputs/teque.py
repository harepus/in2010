from collections import deque
import sys


class Teque:
    def __init__(self):
        self.front = deque()
        self.back = deque()

    def push_back(self, x):
        self.back.append(x)
        self.sort()

    def push_front(self, x):
        self.front.appendleft(x)
        self.sort()

    def push_middle(self, x):
        total_len = len(self.front) + len(self.back)
        if len(self.front) <= total_len // 2:
            self.front.append(x)
        else:
            self.back.appendleft(x)
        self.sort()

    def sort(self):
        while len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())
        while len(self.back) > len(self.front):
            self.front.append(self.back.popleft())

    def get(self, i):
        if i < len(self.front):
            return self.front[i]
        else:
            return self.back[i - len(self.front)]


if __name__ == "__main__":

    teque = Teque()
    line = sys.stdin.readline()

    for i in range(int(line.strip())):
        line = sys.stdin.readline()
        command, argument = line.split(" ")
        argument = int(argument)

        if command == "push_back":
            teque.push_back(argument)
        elif command == "push_front":
            teque.push_front(argument)
        elif command == "push_middle":
            teque.push_middle(argument)
        elif command == "get":
            sys.stdout.write(f"{teque.get(argument)}\n")
