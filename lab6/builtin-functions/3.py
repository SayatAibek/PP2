def ispalindrome(s):
    s=s.lower()
    return s==s[::-1]
print(ispalindrome("abc"))
print(ispalindrome("aba"))
print(ispalindrome("AbBa"))
print(ispalindrome("aacCcAa"))
