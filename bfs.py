from queue import PriorityQueue
v=14
graph=[[] for i in range(v)]
def addedge(x,y,cost):
    graph[x].append((y,cost))
    graph[y].append((x,cost))
def bestFirstSearch(source,target,n):
    visted=[False]*n
    pq=PriorityQueue()
    pq.put((0,source))
    visted[source]=True
    while pq.empty()==False:
        u=pq.get()[1]
        print(u,end=" ")
        if(u==target):
            break
        for v,c in graph[u]:
            if(visted[v]==False):
                visted[v]=True
                pq.put((c,v))
    print()
n=int(input("Enter the no of edges"))
print("Enter the edges and their cost")
for i in range(n):
    a,b,c=map(int,input().split())
    addedge(a,b,c)
source=int(input("Enter the source"))
target=int(input("Enter the target"))
bestFirstSearch(source,target,v)
