"""
As we want to print output of a specific key(studemt) so we use dictionary in this
"""
if __name__ == '__main__':                 #pre written
    n = int(input())                       #pre written
    student_marks = {}                     #pre written
    for i in range(n):                     #pre written
        name, *line = input().split()      #pre written
        scores = list(map(float, line))    #pre written
        student_marks[name] = scores       #pre written
    query_name = input()                   #pre written
    s=0                                    #defining sun to 0
    for i in student_marks[query_name]:    #calling key(student name) in dictionary and iterating on value(list of numbers)
        s+=i                               #adding values in list(marks of a student)
        
    k = len(student_marks[query_name])     # finding length of list value
    s =s/k                                 # calculating average of marks
    print("{0:.2f}".format(s))             #formated string