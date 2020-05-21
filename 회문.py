T=int(input())
for i in range(T):
    result=[]
    result2=[]
    N,M=map(int, input().split())
    for j in range(N):
        result.append(input())
    for j in range(N):
        for k in range(N-M+1):
            temp=''
            for l in range(M):
                temp+=result[j][k+l]
            if temp == temp[::-1]:
                r=temp
    for j in range(N):
        for k in range(N-M+1):
            temp=''
            for l in range(M):
                temp+=result[k+l][j]
            if temp == temp[::-1]:
                r=temp
    print("#%d %s" % (i+1,r))
