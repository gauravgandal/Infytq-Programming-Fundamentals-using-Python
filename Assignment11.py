#lex_auth_012693819159732224162

def check_palindrome(word):
    if word[::-1]==word:
        return 1
    else:
        return 0
    #Remove pass and write your logic here

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")