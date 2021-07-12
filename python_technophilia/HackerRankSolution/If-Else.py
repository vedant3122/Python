if __name__ == '__main__':
    n = int(input())
    if(n%2==0):                  # if n is even
        if(n>=2 and n<=5):       # conditional statements when n is even
            print("Not Weird")
        elif(n>=6 and n<=20):
            print("Weird")
        else:
            print("Not Weird")
    else:                        # if n is odd
        print("Weird")    