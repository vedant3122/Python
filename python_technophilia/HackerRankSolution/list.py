if __name__ == '__main__':
    N = int(input())
    k = []
    for i in range(N):
        p = input().split()
        if(p[0]=='insert'):
            k.insert(int(p[1]),int(p[2]))
        elif(p[0]=='print'):
            print(k)
        elif(p[0]=='remove'):
            k.remove(int(p[1]))   
        elif(p[0]=='append'):
            k.append(int(p[1])) 
        elif(p[0]=='sort'):
            k.sort() 
        elif(p[0]=='pop'):
            k.pop()
        elif(p[0]=='reverse'):
            k.reverse()
