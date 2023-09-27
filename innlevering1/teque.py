from collections import deque


class Teque:
    def __init__(self):
        self.front = deque()
        self.back = []
        self.middle = []

    def push_back(self, x):
        self.back.append(x)
        if len(self.back) > len(self.front):
            self.front.append(self.middle.pop())

    def push_front(self, x):
        self.front.append(x)
        if len(self.front) > len(self.back) + 1:
            self.middle.append(self.front.pop())

    def push_middle(self, x):
        self.middle.append(x)
        if len(self.middle) > len(self.front):
            self.front.append(self.middle.pop())
        if len(self.middle) > len(self.back):
            self.back.append(self.middle.pop())

    def get(self, i):
        if i < len(self.front):
            return self.front[i]
        i -= len(self.front)
        if i < len(self.middle):
            return self.middle[i]
        i -= len(self.middle)
        return self.back[i]
