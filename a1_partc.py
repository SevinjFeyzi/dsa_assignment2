class Stack:

    def __init__(self, cap=10):
        self._capacity = cap
        self.data = []

    def capacity(self):
        return self._capacity
    
    def push(self, data):
        if len(self.data) >= self._capacity:
            self._capacity *= 2
        self.data.append(data)


    def pop(self):
        if self.data:
            return self.data.pop()
        else:
            raise IndexError("pop() used on empty stack")

    def get_top(self):
        if self.data:
            return self.data[-1]
        else:
            return None

    def is_empty(self):
        return not bool(self.data)

    def __len__(self):
        return len(self.data)


class Queue:

    def __init__(self, cap=10):
        self._capacity = cap
        self.data = []

    def capacity(self):
        return self._capacity

    def enqueue(self, data):
        if len(self.data) >= self._capacity:
            self._capacity *= 2
        self.data.append(data)
    
    def dequeue(self):
        if self.data:
            return self.data.pop(0)
        else:
            raise IndexError("dequeue() used on empty queue")

    def get_front(self):
        if self.data:
            return self.data[0]
        else:
            return None 

    def is_empty(self):
        return not bool(self.data)

    def __len__(self):
        return len(self.data)


class Deque:

    def __init__(self, cap=10):
        self._capacity = cap
        self.data = []

    def capacity(self):
        return self._capacity

    def push_front(self, data):
        if len(self.data) >= self._capacity:
            self._capacity *= 2
        self.data.insert(0, data)

    def push_back(self, data):
        if len(self.data) >= self._capacity:
            self._capacity *= 2
        self.data.append(data)



    def pop_front(self):
        if self.data:
            return self.data.pop(0)
        else:
            raise IndexError("pop_front() used on empty deque")

    def pop_back(self):
        if self.data:
            return self.data.pop()
        else:
            raise IndexError("pop_back() used on empty deque")

    def get_front(self):
        if self.data:
            return self.data[0]
        else:
            return None 

    def get_back(self):
        if self.data:
            return self.data[-1]
        else:
            return None

    def is_empty(self):
        return not bool(self.data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, k):
        if k < 0 or k >= len(self.data):
            raise IndexError("Index out of range")
        return self.data[k]
