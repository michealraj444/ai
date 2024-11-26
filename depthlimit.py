from collections import defaultdict
graph=defaultdict(list)
v=set()
path=list()
def addedge(a,b):
    graph[a].append(b)
    graph[b].append(a)
def dfs(n,target,depth):
    path.append(n)
    if n==target:
        return True
    if depth<0:
        return
    if n not in v:
        v.add(n)
        for i in graph[n]:
            if i not in v:
                if dfs(i,target,depth-1)==True:
                    return True
                path.remove(i)
n=int(input("Enter the no of edges"))
print("Enter the edges")
for i in range(n):
    a,b=map(int,input().split())
    addedge(a,b)
target=int(input("Enter the target"))
depth=int(input("Enter the max depth"))
source=int(input("Enter the source"))
if dfs(source,target,depth)==True:
    print("Target can be reached from source within max depth")
    print("Path : ",path)
else:
    print("Unable to reach target")
