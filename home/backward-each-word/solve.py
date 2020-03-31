'''
https://py.checkio.org/en/mission/backward-each-word/

In a given string you should reverse every word, but the words should stay in their places.

Input: A string.

Output: A string.

Example:

backward_string_by_word('') == ''
backward_string_by_word('world') == 'dlrow'
backward_string_by_word('hello world') == 'olleh dlrow'
backward_string_by_word('hello   world') == 'olleh   dlrow'

Precondition: The line consists only from alphabetical symbols and spaces.

'''

def backward_string_by_word(text: str) -> str:
    # list comprehension of splited 'text' with ' ' to get each word individually
    # reverse the word using slicing ::-1 (get entire array with increment -1)
    # join the reversed word with ' '
    return ' '.join([word[::-1] for word in text.split(' ')])


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
