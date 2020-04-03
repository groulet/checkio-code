'''
https://py.checkio.org/en/mission/end-zeros/

Try to find out how many zeros a given number has at the end.

Input: A positive Int

Output: An Int.

Example:

end_zeros(0) == 1
end_zeros(1) == 0
end_zeros(10) == 1
end_zeros(101) == 0

'''

# Other possibility: use regex "0+$", do some math and loop with mod

def end_zeros(num: int) -> int:
    # your code here
    for i in range(1,len(str(num))+1):
        if str(num)[-i:] != '0'*i:
            return i-1
    return i

if __name__ == '__main__':
    print("Example:")
    print(end_zeros(100100))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
