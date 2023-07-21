import sys
import ctypes # It provides C compatible datatypes

class MyList:

    def __init__(self):
        self.size = 1
        self.items = 0

        # create a C type array with size = self.size
        self.array = self.__create_array(self.size)


    def __create_array(self, capacity):
        # creates a ctype array (fixed size) with size capacity
        return (capacity * ctypes.py_object)()
    
    def __len__(self):
        return self.items
    
    def __str__(self):
        output = ''
        for i in range(self.items):
            output = output + str(self.array[i]) + ','
        return '[' + output[:-1] + ']'
    
    def append(self, item):
        if self.size == self.items:
            # resize by 2 object's location
            self.__resize(self.size + 2)
            
        # append on nth position and inc by 1
        self.array[self.items] = item  
        self.items = self.items + 1

    def __resize(self, new_capacity):
        # create a new array with new capacity
        array2 = self.__create_array(new_capacity)
        self.size = new_capacity
        # copy the content of A to B
        for i in range(self.items):
            array2[i] = self.array[i]
        self.array = array2

L = MyList()
print(type(L))


for i in range(0,10):
    L.append(i)
    print(L, sys.getsizeof(L))