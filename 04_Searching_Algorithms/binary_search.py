array = [26,32,50,56,73,87,94,100]

def binary_search(array, low, high, item):
    
    # print(f'low = {low} high = {high}', end = ' ')
    if low <= high:
        mid_index = (low + high) // 2
        # print('mid value = ', mid_index)
        if array[mid_index] == item:
            return mid_index
        elif array[mid_index] > item:
            return binary_search(array, low, mid_index - 1, item)
        else:
            return binary_search(array, mid_index + 1, high, item)
    else:
        return 'not found'

print(binary_search(array, 0, len(array)-1, 100))