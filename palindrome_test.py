def palindrome_check(_):
    return _ == _[::-1]


s = input("String: ")
ans = palindrome_check(s)

if ans:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")
