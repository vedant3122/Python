# function for checking leap year
def is_leap(year):
    leap = False
    
    # function logic
    if (year%400 == 0):                              
        leap = True
    elif(year%4 == 0 and year%100 != 0):
        leap = True
    return leap

# cheaking whether year is leap year or not using above defined function
year = int(input())   
print(is_leap(year))


"""
we can also write above function as
"""
    # def is_leap(year):
    #     leap = False
         
    #     if (year%400 == 0 or (year%4 == 0 and year%100 != 0)):
    #         leap = True
    
    #     return leap

