T=int(input())
result=[]
for i in range(T):
    N=input()
    M=input()
    if N in M:
        r=1
    else:
        r=0
    print("#%d %d" % (i+1,r) )
