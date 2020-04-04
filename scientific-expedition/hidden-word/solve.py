'''
https://py.checkio.org/en/mission/hidden-word/

Nicola has solved this puzzle (and I am sure that you will do equally well).
To be prepared for more such puzzles, Nicola wants to invent a method to
search for words inside poetry. You can help him create a function to search
for certain words.

You are given a rhyme (a multiline string), in which lines are separated by "newline" (\n).
Casing does not matter for your search, but whitespaces should be removed before your search.
You should find the word inside the rhyme in the horizontal (from left to right)
or vertical (from up to down) lines. For this you need envision the rhyme as a matrix (2D array).
Find the coordinates of the word in the cut rhyme (without whitespaces).

The result must be represented as a list -- [row_start,column_start,row_end,column_end], where

row_start is the line number for the first letter of the word.
column_start is the column number for the first letter of the word.
row_end is the line number for the last letter of the word.
column_end is the column number for the last letter of the word.
Counting of the rows and columns start from 1.
rhymes
Input: Two arguments. A rhyme as a string and a word as a string (lowercase).

Output: The coordinates of the word.

Example:

checkio(u"""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", u"ten") == [2, 14, 2, 16]
checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
    
How it is used: This task shows the variance of the positional ciphers. With this cipher you can hide a message within a book which allows you and receiver to send these coded messages.

Precondition: The word is given in lowercase
0 < |word| < 10
0 < |rhyme| < 300
'''

def checkio(text, word):
    # remove whitespaces and split by line
    arr = [line for line in text.lower().replace(' ','').split('\n')]
    # make each lines the same length
    max_line_len = len(max(arr,key=len))
    arr = [line+'#'*(max_line_len-len(line)) for line in arr]
    # loop over each row
    for row in range(len(arr)):
        # search for 'word' in each row
        col = arr[row].find(word)
        if col >= 0:
            return [row+1,col+1,row+1,col+len(word)]
    # rotate array (list(zip(*arr))) by unpacking each line (*arr)
    # "zip" them together (zip(...))
    # join the line to make a string ''.join(...)
    arr = [''.join(col) for col in list(zip(*arr))]
    # loop over each column
    for col in range(len(arr)):
        # search for 'word' in each column
        row = arr[col].find(word)
        if row >= 0:
            return [row+1,col+1,row+len(word),col+1]
    return None

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
    assert checkio("Twas brillig, and the slithy toves\nDid gyre and gimble in the wabe;\nAll mimsy were the borogoves,\nAnd the mome raths outgrabe.","stog") == [1,19,4,19]

