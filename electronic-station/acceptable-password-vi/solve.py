'''
https://py.checkio.org/en/mission/acceptable-password-vi/

In this mission you need to create a password verification function.

Those are the verification conditions:

the length should be bigger than 6;
should contain at least one digit, but it cannot consist of just digits;
having numbers or containing just numbers does not apply to the password longer than 9.
a string should not contain the word "password" in any case;
should contain 3 different letters (or digits) even if it is longer than 10
Input: A string.

Output: A bool.

Example:

is_acceptable_password('short') == False
is_acceptable_password('short54') == True
is_acceptable_password('muchlonger') == True
is_acceptable_password('ashort') == False
is_acceptable_password('muchlonger5') == True
is_acceptable_password('sh5') == False
is_acceptable_password('1234567') == False
is_acceptable_password('12345678910') == True
is_acceptable_password('password12345') == False
is_acceptable_password('PASSWORD12345') == False
is_acceptable_password('pass1234word') == True
is_acceptable_password('aaaaaa1') == False
is_acceptable_password('aaaaaabbbbb') == False

How it’s used: For password verification form. Also it's good to learn how the task can be evaluated.
'''
def is_acceptable_password_1(password: str) -> bool:
    return len(password) > 6

def is_acceptable_password_2(password: str) -> bool:
    return any([c.isdigit() for c in password])

def is_acceptable_password_3(password: str) -> bool:
    return not password.isdigit()

def is_acceptable_password_4(password: str) -> bool:
    return len(password) > 9

def is_acceptable_password_5(password: str) -> bool:
    return (not "password" in password.lower())

def is_acceptable_password_6(password: str) -> bool:
    return len(set(password)) >= 3

def is_acceptable_password(password: str) -> bool:
    # the length should be bigger than 6;
    if not is_acceptable_password_1(password): 
        return False

    # should contain at least one digit, but it cannot consist of just digits;
    # having numbers or containing just numbers does not apply to the password longer than 9.
    if not is_acceptable_password_4(password) and not (is_acceptable_password_2(password) and is_acceptable_password_3(password)):
        return False

    # a string should not contain the word "password" in any case;
    if not is_acceptable_password_5(password):
        return False

    # should contain 3 different letters (or digits) even if it is longer than 10
    if not is_acceptable_password_6(password):
        return False
    
    return True

if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('short54') == True
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    assert is_acceptable_password('12345678910') == True
    assert is_acceptable_password('password12345') == False
    assert is_acceptable_password('PASSWORD12345') == False
    assert is_acceptable_password('pass1234word') == True
    assert is_acceptable_password('aaaaaa1') == False
    assert is_acceptable_password('aaaaaabbbbb') == False
    assert is_acceptable_password('aaaaaabb1') == True
    assert is_acceptable_password('abc1') == False
    assert is_acceptable_password('abbcc12') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
