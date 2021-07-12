"""
METHOD - 1
[Here only the code of function to capitalise not to print new string]
"""

def solve(s):
    string = ""                          #creating a string to store capitalize string
    for i in range(len(s)):
        if i==0:                         #capitalizing first letter of given string
            string+=s[i].capitalize()  
            continue
        if(s[i-1]== ' '):               #check for space if space was present
            string+=s[i].capitalize()   #then capitalizing next letter after space
            continue
        string+=s[i]
    return string


"""
METHOD - 2
[Here only the code of function to capitalise not to print new string]
"""


def solve(s):
    for x in s[:].split():
       s=s.replace(x,x.capitalize())
    return s



