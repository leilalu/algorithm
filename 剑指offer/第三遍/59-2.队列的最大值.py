class MaxQueue:
    def __init__(self):
        from collections import deque
        self.data = deque()
        self.max_data = deque()

    def max_value(self):
        return self.max_data[0] if self.max_data else -1

    def push_back(self, value):
        self.data.append(value)

        while self.max_data and value > self.max_data[-1]:
            self.max_data.pop()
        self.max_data.append(value)

    def pop_front(self):
        if self.data and self.max_data:
            res = self.data.popleft()
            if res == self.max_data[0]:
                self.max_data.popleft()
            return res
        else:
            return -1
