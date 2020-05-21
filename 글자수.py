T=int(input())
for i in range(T):
    N=list(set(input()))
    M=list(input())
    result=[]
    for j in range(len(M)):
        if M[j] in N:
            result.append(M.count(M[j]))
    print("#%d %d" % (i+1, max(result)) )
