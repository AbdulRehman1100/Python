
def binary_search(array, value):
    '''
    Return index of value in a sorted, indexable sequence using binary search.

    - array must be sorted in ascending order; results are undefined
      (unreliable) if it is not.
    - If storing user-defined objects, those objects must implement
      __lt__ and __eq__ for comparison; otherwise TypeError will be
      raised.
    - Return -1 if value is not found.
    '''
    start_index = 0
    end_index = len(array) - 1

    while start_index <= end_index:
        mid = (start_index + end_index)//2
        if value == array[mid]:
            return mid
        elif value < array[mid]:
            end_index = mid - 1 
        else:
            start_index = mid + 1
    return -1