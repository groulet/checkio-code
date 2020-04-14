'''
https://py.checkio.org/en/mission/conversion-from-camelcase/

Your mission is to convert the name of a function (a string) from CamelCase ("MyFunctionName") into the Python format ("my_function_name") where all chars are in lowercase and all words are concatenated with an intervening underscore symbol "_".

Input: A function name as a CamelCase string.

Output: The same string, but in under_score.

Example:

from_camel_case("MyFunctionName") == "my_function_name"
from_camel_case("IPhone") == "i_phone"
from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
from_camel_case("Name") == "name"

How it is used: To apply function names in the style in which they are adopted in a specific language (Python, JavaScript, etc.).

Precondition:
0 < len(string) <= 100
Input data won't contain any numbers.
'''
import re
def from_camel_case(name):
    # using regex:
    #name[0].lower() + re.sub(r'([A-Z])',lambda m: '_'+m.group(0).lower(),name[1:])
    
    return ''.join([name[0].lower()] + ['_'+l.lower() if l.isupper() else l for l in name[1:]])

if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("Name"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")

