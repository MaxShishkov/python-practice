def reverse(text):
    if len(text) == 1:
        return text
    else:
        return text[- 1] + reverse(text[:-1])
        
        
print reverse("abcd")

"""
def reverse(text):
    rev_str = ""
    length = len(text) - 1
    for i in range(0,length + 1):
        print i
        rev_str+=text[length - i]
    return rev_str
        
        
print reverse("abcd")
"""