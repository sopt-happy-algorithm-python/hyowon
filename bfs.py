import sys

n,m,v=map(int, sys.stdin.readline().split())
b=[list() for i in range(n+1)]
for i in range(m):
    x,y=map(int, sys.stdin.readline().split())
    b[x].append(y)
    b[y].append(x)
for i in range(len(b)):
    b[i].sort()
def bfs(a):
    result=""
    q=[a]
    visited=[False]*(n+1)
    while q:
        for i in range(len(q)):
                v=q.pop(0)
                for i in range(len(b[v])):
                    if not visited[b[v][i]]:
                        q.append(b[v][i])
                if visited[v]==False:
                    visited[v]=True
                    result+=str(v)+" "
    return result

print(bfs(v))
