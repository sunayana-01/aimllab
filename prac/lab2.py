def compute_min(v):
    min_cost=0
    min_cost_path=[]
    flag=True

    for children in graph.get(v, ''):
        nodelist=[]
        cost=0
        for m, weight in children:
            cost+=weight+h[m]
            nodelist.append(m)
        
        if flag==True:
            min_cost=cost
            min_cost_path=nodelist
            flag=False
        elif cost<min_cost:
            min_cost=cost
            min_cost_path=nodelist
        
    return min_cost, min_cost_path


def aostaralgo(start, v, backtracking):
    print('Current Node:', v)
    print('Heuristic values:', h)
    print('Solution graph:', solution_graph)
    print('------------------------------------------------------------------------------------------------------------------------')
    if status.get(v,0)>=0:
        cost, list = compute_min(v)
        h[v]=cost
        status[v]=len(list)
        solved = True

        for n in list:
            parent[n]=v
            if status.get(n, 0)!=-1:
                solved=solved&False

        if solved:
            status[v]=-1
            solution_graph[v]=list

        if v!=start:
            aostaralgo(start, parent[v], True)
        if not backtracking:
            for child in list:
                aostaralgo(start, child, False)
        
h = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 2, 'F': 1, 'G': 5, 'H': 7, 'I': 7, 'J': 1, 'T': 3}
graph = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],
    'B': [[('G', 1)], [('H', 1)]],
    'C': [[('J', 1)]],
    'D': [[('E', 1), ('F', 1)]],
    'G': [[('I', 1)]]
}
parent={}
solution_graph={}
status={}
aostaralgo('A', 'A', False)
print()
print('Solution:')
print(solution_graph)