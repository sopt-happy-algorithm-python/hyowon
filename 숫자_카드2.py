import sys
from collections import Counter
a=sys.stdin.readline()
e=list(sys.stdin.readline().split())
b=sys.stdin.readline()
q=list(sys.stdin.readline().split())
c=Counter(e)
for i in q:
    print(c[i], end=" ")
