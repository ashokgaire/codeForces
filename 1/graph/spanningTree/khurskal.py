

def mark_set(parent,rank,vertice):
    parent[vertice] =  vertice
    rank[vertice] = 0

def find(parent,i):
    while parent[i] != i:
        parent[i] = parent[parent[i]]
        i = parent[i]
    return i

def union(parent, rank , u, v):
    roota = find(parent,u)
    rootb = find(parent,v)

    if roota != rootb:
        if rank[roota] < rank[rootb]:
            parent[roota] = parent[rootb]
        else:
            parent[rootb] = parent[roota]
        
        if rank[roota] == rank[rootb]:
            rank[rootb] +=1


def kruskal(graph):
    
    parent = dict()
    rank = dict()
    for vertice in graph["vertices"]:
        mark_set(parent,rank,vertice)
    minimum_spaning_tree = []
    edges = list(graph["edges"])
    edges.sort()

    for edge in edges:
        w , u , v = edge
        if find(parent,u)  != find(parent,v):
            union(parent, rank, u,v)
            minimum_spaning_tree.append(w)
    return sum(minimum_spaning_tree)



if __name__ == "__main__":
    n,m = map(int,input().split())
    graph = {"vertices":set(),"edges":set([])}
    
    while m > 0:
        u,v,c = map(int, input().split())
        graph["vertices"].add(u)
        graph["vertices"].add(v)
        graph["edges"].add((c,u,v))
        m -=1

    
    cost = kruskal(graph)
    print(cost)

