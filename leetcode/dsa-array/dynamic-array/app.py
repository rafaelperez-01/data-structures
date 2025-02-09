class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        if i >= self.length or i < 0:
            raise IndexError("Index out of bounds")
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i >= self.length or i < 0:
            raise IndexError("Index out of bounds")
        self.arr[i] = n

    def insert(self, i: int, n: int) -> None:
        if i < 0 or i > self.length:
            raise IndexError("Index out of bounds")
        if self.length == self.capacity:
            self.resize()
        for index in range(self.length - 1, i - 1, -1):
            self.arr[index + 1] = self.arr[index]
        self.arr[i] = n
        self.length += 1

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length == 0:
            raise IndexError("Pop from empty array")
        temp = self.arr[self.length - 1]
        self.arr[self.length - 1] = 0
        self.length -= 1
        return temp

    def resize(self) -> None:
        self.capacity *= 2
        new_array = [0] * self.capacity
        for i in range(self.length):
            new_array[i] = self.arr[i]
        self.arr = new_array

    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity

