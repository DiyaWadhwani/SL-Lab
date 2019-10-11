def letterSurround(s):
    str1=list(s)
    if str1[0].isalpha() or str1[-1].isalpha():
        return False
    for i in range(0,len(s)):
        if str1[i].isalpha():
            if str1[i-1]=='+' and str1[i+1]=='+':
                continue
            else:
                return False
    return True
s=str(input("Enter string: "))
print(letterSurround(s))
