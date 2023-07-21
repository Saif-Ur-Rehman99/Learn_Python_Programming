import ctypes # It provides C compatible datatypes

class MyList:

    def __init__(self):
        self.size_of_array = 1
        self.items_in_array = 0

        # create a C type array with size = self.size
        self.array = self.__create_array(self.size_of_array)


    def __create_array(self, capacity):
        # creates a ctype array (fixed size) with size capacity
        return (capacity * ctypes.py_object)()
    
    def __len__(self):
        return self.items_in_array
    
    def append(self, item):
        if self.size_of_array == self.items_in_array:
            # resize by 2 object's location
            self.__resize(self.size_of_array + 2)
            
        # append
        self.array[self.items_in_array] = item
        self.items_in_array = self.items_in_array + 1

    def __resize(self, new_capacity):
        # create a new array with new capacity
        self.__create_array(new_capacity)
        self.size_of_array = new_capacity
        # copy the content of A to B
        for i in range(self.items_in_array):
            arrayB[i] = self.array[i]
        self.array = arrayB

L = MyList()
print(type(L))
print(len(L))
