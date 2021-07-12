if __name__ == '__main__':
    n = int(input())                    #taking input of number of scores
    arr = map(int, input().split())     #taking input of marks into array
    print(sorted(list(set(arr)))[-2])   
    """
    conveting array into list and sorted the 
    list as we want second highest so its index is [-2]
    """


