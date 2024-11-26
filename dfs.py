from collections import defaultdict
graph=defaultdict(list)
v=set()
def addedge(a,b):
    graph[a].append(b)
    graph[b].append(a)
def dfs(n):
    if n not in v:
        v.add(n)
        print(n,end=" ")
        for i in graph[n]:
            if i not in v:
                dfs(i)

n=int(input("Enter the no of edges"))
print("Enter the edges")
for i in range(n):
    a,b=map(int,input().split())
    addedge(a,b)
print("The DFS Sequence is :",end=" ")
dfs(1)
