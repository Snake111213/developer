'''def is_palindrome(this_str):
    rev_str = this_str[::-1]
    if (this_str == rev_str):
        return True
    else:
        return False
is_palindrome("racerar")
True'''


def is_palindrome(this_str):
    rev_str = ''.join(reversed(this_str))
    if (this_str== rev_str):
        return True
    else:
        return False
    
is_palindrome('')

str_list = ['refer','blue','level','123321','dragon']

palindromes = [string for string in str_list if is_palindrome(string)]
print(palindromes)