'''
https://py.checkio.org/en/mission/goes-after/

In a given word you need to check if one symbol goes after another.

Cases you should expect while solving this challenge:

one of the symbols are not in the given word - your function should return False;
any symbol appears in a word more than once - use only the first one;
two symbols are the same - your function should return False;
the condition is case sencetive, which mease 'a' and 'A' are two different symbols.
Input: Three arguments. The first one is a given string, second is a symbol that shoud go first, and the third is a symbold that should go after the first one.

Output: A bool.

Example:

goes_after('world', 'w', 'o') == True
goes_after('world', 'l', 'o') == False
goes_after('panorama', 'a', 'n') == True
goes_after('list', 'l', 'o') == False
goes_after('', 'l', 'o') == False
goes_after('list', 'l', 'l') == False
'''

def goes_after(word: str, first: str, second: str) -> bool:
    return 0 < (word.find(second) - word.find(first)) <= word.find(second)


if __name__ == '__main__':
    print("Example:")
    print(goes_after('world', 'w', 'o'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert goes_after('world', 'w', 'o') == True
    assert goes_after('world', 'l', 'o') == False
    assert goes_after('panorama', 'a', 'n') == True
    assert goes_after('list', 'l', 'o') == False
    assert goes_after('', 'l', 'o') == False
    assert goes_after('list', 'l', 'l') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
