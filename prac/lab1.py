def astaralgo(start, stop):
    open=set()
    close=set()
    dist={}
    parent={}
    open.add(start)
    dist[start]=0
    parent[start]=start

    while len(open)>0:
        n=None

        for v in open:
            if n==None or dist[v]+H[v]<dist[n]+H[n]:
                n=v
        
        if n==stop:
            path=[]
            while parent[n]!=n:
                path.append(n)
                n=parent[n]
            path.append(start)
            path.reverse()
            print("Path found:", path)
            return path
        
        if n==None:
            print("Path does not exist.")
            return None
        
        if graph[n]!=None:
            for m,weight in graph[n]:
                if m not in open and m not in close:
                    parent[m]=n
                    open.add(m)
                    dist[m]=dist[n]+weight
                elif dist[m]>dist[n]+weight:
                    dist[m]=dist[n]+weight
                    open.add(m)
                    if m in close: close.remove(m)

        open.remove(n)
        close.add(n)

    print('Path not found.')
    return None

graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1),('H', 7)] ,
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)],
}

H = {
    'A': 10,
        'B': 8,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0
}

astaralgo('A', 'J')
