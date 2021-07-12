"""
METHOD - 1
"""

def swap_case(s):
    k = list(s)                 #convert element of s into list
    for i in range(len(s)):     #check on each element of list
        if k[i].isupper():            
            k[i] = k[i].lower()
        else:
            k[i] = k[i].upper()
    s=""
    for i in k:
        s+=i              #coverting swap case list into string
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

"""
METHOD - 2
"""


"""
python also has inbuild function
"""
#(swapcase()) 
"""
to swap case we can dirctly use it
"""

def swap_case(s):
    
    return s.swapcase()  #direcly using inbuild "swapcase" function

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
