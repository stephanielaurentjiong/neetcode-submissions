class DynamicArray:
    
    def __init__(self, capacity: int):
        # The number of boxes
        self.capacity = capacity
        # The number of elements currently have
        self.size = 0
        # Create the array 
        self.arr = [0] * capacity
        

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # Check if the boxes are available
        if (self.capacity == self.size):
            # Increase the size 
            self.resize()

        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        # Soft pop
        if (self.size > 0):
            self.size -= 1

        return self.arr[self.size]

    def resize(self) -> None:
        self.capacity = 2 * self.capacity

        new_arr = [0] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr


    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
