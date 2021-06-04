class Node:
    def __init__(self, arg_id):
        self._id = arg_id



def PrimsMST(graph):
    priority_queue = {Node(0):0}
    added = [False]*len(graph)
    min_cost = 0

    while priority_queue:
        node = min(priority_queue, key = priority_queue.get)
        cost = priority_queue[node]
        del priority_queue[node]

        if added[node._id] == False:
            min_cost +=cost
            added[node._id] = True

            for item in graph[node._id]:
                adjnode = item[0]
                adjcost = item[1]
                if added[adjnode] == False:
                    priority_queue[Node(adjnode)] = adjcost

    return min_cost


if __name__ == "__main__":
    n,m = map(int,input().split())
    graph = [[] for _ in range(n)]
    
    while m > 0:
        u,v,c = map(int, input().split())
        graph[u-1].append((v-1,c))
        graph[v-1].append((u-1,c))
        m -=1
    print(PrimsMST(graph))

