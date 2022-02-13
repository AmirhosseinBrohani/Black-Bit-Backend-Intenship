import re

regex = r'\b[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[A-Z|a-z]{,3}\b'

def fun(s):
    # return True if s is a valid email, else return False
    if(re.fullmatch(regex, s)):
        return True
 
    else:
        return False