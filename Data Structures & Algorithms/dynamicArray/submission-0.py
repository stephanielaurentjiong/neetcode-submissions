class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    #Set n at i-th index
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
        
    #Insert value n in the last position 
    def pushback(self, n: int) -> None:
        if (self.capacity == self.size):
            self.resize()

        self.arr[self.size] = n
        self.size += 1

    # Remove the last element in the array
    def popback(self) -> int:
        if self.size > 0:
            self.size -= 1

        return self.arr[self.size]
        

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_arr = [0] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        #Get the size of the boxes that "have a value", not including the boxes that doesn't have a value
        return self.size
    
    def getCapacity(self) -> int:
        #Get the length of the container (no the value)
        return self.capacity