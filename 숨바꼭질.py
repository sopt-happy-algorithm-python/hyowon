import sys
n,k=map(int, sys.stdin.readline().split())
def bfs(n):
    q=[n]
    visited=[False]*100001
    count=0
    state=False
    while q:
        for i in range(len(q)):
            v=q.pop(0)
            if not(visited[v]):
                visited[v]=True
                if v+1<=100000:
                    q.append(v+1)
                if v-1>=0:
                    q.append(v-1)
                if v*2<=100000:
                    q.append(v*2)
                if v==k:
                    state=True
                    break
        if state:
            print(count)
            break
        count+=1
bfs(n)
