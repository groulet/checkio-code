# First tasks. check if all elements are the same

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # if size is 0 return True
    if len(elements) > 0:
        # get the first element
        first = elements[0]
        # check is all elemtns are equal to the first elemnt
        for e in elements:
            # stop if one element is diffirent and return false
            if e != first:
                return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")