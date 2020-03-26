'''
https://py.checkio.org/mission/sort-array-by-element-frequency/solve/

Sort the given iterable so that its elements end up in the decreasing
frequency order, that is, the number of times they appear in elements.
If two elements have the same frequency, they should end up in the same
order as the first appearance in the iterable.

Input: Iterable

Output: Iterable

Precondition: elements can be ints or strings

The mission was taken from Python CCPS 109 Fall 2018. It's being taught
for Ryerson Chang School of Continuing Education by Ilkka Kokkarinen
'''
from operator import itemgetter

def frequency_sort(items):
    # get a set with unique items
    col = set(items)
    # create tuples with item, count item in items and index in items
    # sort the list over over count and index
    # Set position with -1* for reverse sorting
    sorted_col = sorted(zip(col,map(items.count,col),map(lambda x: -1*items.index(x),col)),key=itemgetter(1,2),reverse=True)
    r=()
    for i in sorted_col:
        r = [*r,*[i[0]]*i[1]]
    return r


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
