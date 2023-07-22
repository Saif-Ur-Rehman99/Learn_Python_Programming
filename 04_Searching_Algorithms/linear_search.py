array = [10,92,23,74,55,36,17,86,95,30]

def linear_search(array, item):
    for i in range(len(array)):
        if array[i] == item:
            return i
    return 'not found'


print(linear_search(array, 80))