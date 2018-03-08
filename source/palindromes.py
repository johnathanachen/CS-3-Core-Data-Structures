#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""

    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):

    # clean them up
    cleaned_text = __magic_wand(text)

    # set the pointers
    leading = 0
    trailing = len(cleaned_text) - 1

    while(leading <= trailing):
        # check if both half matches split from the middle
        if(cleaned_text[leading] != cleaned_text[trailing]):
            return False

        # move one step closer to middle from both sides
        leading += 1
        trailing -= 1

    return True



def is_palindrome_recursive(text, left=None, right=None):

    # clean them up
    cleaned_text = __magic_wand(text)

    # the beginning
    if left is None and right is None:
        # set the pointers
        left = 0
        right = len(cleaned_text) - 1


    # If text is less than 1 or empty then return true
    if len(cleaned_text) < 1 or cleaned_text == '':
        return True
        
    # coming back again
    if left <= right:
        if cleaned_text[left] == cleaned_text[right]:
            # inception mode
            return is_palindrome_recursive(cleaned_text, left=left + 1, right=right - 1)
        else:
            return False
    return True



def __magic_wand(text):
    # remove punc and lower letters
    cleaned_text = ''.join([i for i in text.lower() if i in string.ascii_letters])
    return cleaned_text

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
