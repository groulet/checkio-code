'''
https://py.checkio.org/en/mission/split-pairs/

Split the string into pairs of two characters. If the string contains an odd number of characters, then the missing second character of the final pair should be replaced with an underscore ('_').

Input: A string.

Output: An iterable of strings.

Example:

split_pairs('abcd') == ['ab', 'cd']
split_pairs('abc') == ['ab', 'c_']
1
2
Precondition: 0<=len(str)<=100
'''
def split_pairs(a):
    # append '_' at the end of "a"
    # loop every 2 indexes of "a": 0, 2, 4, ...
    # for loop will stop at i < len(a) =>
    #   range(0, len(''), 2) == range(0,0,2) will not loop and function will return []
    #   range(0, len('abcd'), 2) == range(0,4,2) will loop 0, 2
    #   range(0, len('abc'), 2) == range(0,3,2) will loop 0, 2 (we append '_' to "a" for odd length to be of length len(a)+1)
    
    return [(a+'_')[i:i+2] for i in range(0,len(a),2)]

if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
