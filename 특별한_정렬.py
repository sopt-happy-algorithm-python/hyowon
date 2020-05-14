T=int(input())
for j in range(T):
    N=int(input())
    a=list(map(int, input().split()))
    result=[0]*N
    s=""
    b=sorted(a)
    c=sorted(a, reverse=True)
    for i in range(len(b)//2):
        b.pop()
    for i in range(len(c)//2):
        c.pop()
    for i in range(len(b)):
        result[2*i+1]=b[i]
    for i in range(len(c)):
        result[2*i]=c[i]
    for i in result[:10]:
        s+=str(i)+" "
    print("#%d %s" % (j+1,s))
