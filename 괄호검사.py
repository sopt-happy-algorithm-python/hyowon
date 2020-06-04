a=['}','{',')','(']
t=int(input())
for j in range(t):
    result=[]
    r=[]
    s=input()
    for i in s:
        if i in a:
            result.append(i)
    for i in result:
        if i=='(' or i=='{':
            r.append(i)
        elif i==')' or i=='}':
            if len(r)==0:
                r=[i]
                break
            elif (i==')' and r[-1]!='(') or (i=='}' and r[-1]!='{'):
                r=[i]
                break
            else:
                r.pop()
    if not len(r):
        print(("#%d %d")%(j+1,1))
    else:
        print(("#%d %d")%(j+1,0))  
