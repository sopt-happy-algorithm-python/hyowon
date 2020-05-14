T=int(input())
for i in range(T):
    N=int(input())
    s=[[0]*10 for i in range(10)]
    count=0
    for j in range(N):
        a,b,c,d,e=map(int, input().split())
        for k in range(a,c+1):
            for l in range(b,d+1):
                s[k][l]+=e
    for j in range(10):
        for k in range(10):
            if s[j][k]==3:
                count+=1
    print("#%d %d" % (i+1,count))
