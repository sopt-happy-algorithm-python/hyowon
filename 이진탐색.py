def s(p,a):
    start=1
    end=p
    count=0
    while start<=end:
        mid=(start+end)//2
        if a==mid:
            count+=1
            break
        elif a>mid:
            start=mid
            count+=1
        elif a<mid:
            end=mid
            count+=1
    return count

T=int(input())

for i in range(T):
    P,A,B=map(int, input().split())
    re=s(P,A)
    re1=s(P,B)
    if re<re1:
        result='A'
    elif re>re1:
        result='B'
    else:
        result='0'
    print('#%d %s'% (i+1,result))
