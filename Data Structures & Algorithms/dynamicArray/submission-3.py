class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [0] * capacity
        self.length = 0
        self.capacity = capacity

    def get(self, i: int) -> int:

        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if(self.getSize() == self.getCapacity()):
            self.resize()
        self.set(self.getSize(), n)
        self.length += 1
        
    def popback(self) -> int:
        self.length -= 1
        value = self.array[self.length]
        return value


    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [0] * self.capacity
        for i in range(self.length):
            new_arr[i] = self.array[i]
        self.array = new_arr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity