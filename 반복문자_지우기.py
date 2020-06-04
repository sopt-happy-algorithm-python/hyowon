t=int(input())
for i in range(t):
    a=input()
    j=0
    while True:
        if j==len(a)-1:
            break
        if a[j]==a[j+1]:
            a=a[:j]+a[j+2:]
            j=0
        else:
            j+=1
    print(("#%d %d")%(i+1,len(a)))
