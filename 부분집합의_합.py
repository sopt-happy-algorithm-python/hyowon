from itertools import combinations

A=[]
result=[]
for i in range(1,13):
    A.append(i)
T=int(input())
for j in range(T):
    count=0
    N,K=map(int, input().split())
    for i in range(len(A)+1):
        c=combinations(A,N)
    for i in c:
        if sum(i)==K:
            count+=1
    print("#%d %d" % (j+1, count))
