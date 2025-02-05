class StaticArray:

    def __init__(self):
        self.length = 0
        self.arr = [0] * 7
        self.capacity = len(self.arr)

    def insertEnd(self, value):
        if self.length < self.capacity:
            self.arr[self.length] = value
            self.length += 1
            return True
        return False

    def insertMiddle(self, value, index):

        if index < 0 or index > self.length or self.length == self.capacity:
            return False
        for i in range(self.length - 1, index - 1, -1):
            self.arr[i + 1] = self.arr[i]
        self.arr[index] = value
        self.length += 1
        return True

    def deleteEnd(self):
        if self.length > 0:
            self.arr[self.length - 1] = 0
            self.length -= 1
            return True
        return False

    def removeMiddle(self, index):
        if index < 0 or index >= self.length:
            return False

        for i in range(index + 1, self.length):
            self.arr[i - 1] = self.arr[i]

        self.arr[self.length - 1] = 0
        self.length -= 1
        return True

    def printArr(self):
        for i in range(self.capacity):
            print(self.arr[i])


arr = StaticArray()
arr.insertEnd(1)
arr.insertEnd(2)
arr.insertEnd(3)
arr.insertEnd(4)
arr.insertEnd(5)
arr.removeMiddle(0)
arr.insertMiddle(1, 0)
arr.printArr()