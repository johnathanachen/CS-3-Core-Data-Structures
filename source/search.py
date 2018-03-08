#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index
    return None


def linear_search_recursive(array, item, index=0):
    # check if the search reaches the end
    if index > len(array) - 1:
        return None

    # if item is found, return the index
    if array[index] == item:
        return index

    # move up an index
    return linear_search_recursive(array, item, (index + 1))

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    array = sorted(array)

    # getting into position
    leading = 0
    trailing = len(array) - 1
    in_the_sauce = int(trailing/2)

    # conditions for when item is not found
    if len(array) == 0 or leading > trailing:
        return None
    # when waldo is found
    elif array[in_the_sauce] == item:
        return in_the_sauce

    while array[in_the_sauce] != item and trailing != leading:
        if item < array[in_the_sauce]:
            # new middle has been appointed to the mr.trailing
            trailing = in_the_sauce
            if trailing - leading == 1: # if they're right next to each other
                trailing = leading # the first item in the array
        else:
            # new middle has been appointed to mr.leading
            leading = in_the_sauce
            if trailing - leading == 1: # if they're right next to each other
                leading = trailing # the last item in the array
                in_the_sauce = (trailing - leading) // 2 # returns 0
        in_the_sauce = (trailing + leading) // 2 # returns 0
    if array[in_the_sauce] == item:
        return in_the_sauce
    else:
        return None

def binary_search_recursive(array, item, left=None, right=None):
    sorted_array = sorted(array)

    # ready the edge pointers
    if right is None and left is None:
        left = 0
        right = len(array) - 1
    # didn't find waldo
    if left > right:
        return None
    # if its the first item in the array
    if array[0] == item:
        return 0

    # setting the middle to half of the array
    in_the_sauce = int(left + (right - left) / 2)

    # waldo is in the middle
    if array[in_the_sauce] == item:
        return in_the_sauce

    # to the left to the left
    elif array[in_the_sauce] < item:
        # inception mode
        # get the right half of the array
        return binary_search_recursive(array, item, in_the_sauce+1, right)
    else:
        # get the left half of the array
        return binary_search_recursive(array, item, left, in_the_sauce-1)

if __name__ == '__main__':
    names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
    # linear_search(names, 'Jeremy')
    print(binary_search_recursive(names, 'Brian'))
