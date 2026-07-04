class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * self.capacity
        self.ult = 0


    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:

        if self.ult == self.capacity:
            self.resize()

        self.arr[self.ult] = n
        self.ult += 1

    def popback(self) -> int:
        if self.ult > 0:
            self.ult -= 1
        return self.arr[self.ult]

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        nuevo = [0] * self.capacity

        for i in range(self.ult):
            nuevo[i] = self.arr[i]
        self.arr = nuevo

    def getSize(self) -> int:
        return self.ult
    
    def getCapacity(self) -> int:
        return self.capacity