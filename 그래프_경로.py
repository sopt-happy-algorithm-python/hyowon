def dfs(n):
    chk[n]=True
    answer.append(n)
    for i in result[n]:
        if not chk[i]:
            dfs(i)
            
a=int(input())
for t in range(a):
    answer=[]
    v,e=map(int,input().split())
    result=[list() for _ in range(v+1)]
    for i in range(e):
        start,end=map(int, input().split())
        result[start].append(end)
    s,g=map(int,input().split())
    chk=[False]*(v+1)
    dfs(s)
    if s in answer:
        if g in answer:
            print("#%d %d" % (t+1,1))
        else:
            print("#%d %d" % (t+1,0))
