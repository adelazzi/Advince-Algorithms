graph = [
    [0, 29, 82, 46, 68, 52, 72, 42, 51, 55, 29, 74, 23, 72, 46],
    [29, 0, 55, 46, 42, 43, 43, 23, 23, 31, 41, 51, 11, 52, 21],
    [82, 55, 0, 68, 46, 55, 23, 43, 41, 29, 79, 21, 64, 31, 51],
    [46, 46, 68, 0, 82, 15, 72, 31, 62, 42, 21, 51, 51, 43, 64],
    [68, 42, 46, 82, 0, 74, 23, 52, 21, 46, 82, 58, 46, 65, 23],
    [52, 43, 55, 15, 74, 0, 61, 23, 55, 31, 33, 37, 51, 29, 59],
    [72, 43, 23, 72, 23, 61, 0, 42, 23, 31, 77, 37, 51, 46, 33],
    [42, 23, 43, 31, 52, 23, 42, 0, 33, 15, 37, 33, 33, 31, 37],
    [51, 23, 41, 62, 21, 55, 23, 33, 0, 29, 62, 46, 29, 51, 11],
    [55, 31, 29, 42, 46, 31, 31, 15, 29, 0, 51, 21, 41, 23, 37],
    [29, 41, 79, 21, 82, 33, 77, 37, 62, 51, 0, 65, 42, 59, 61],
    [74, 51, 21, 51, 58, 37, 37, 33, 46, 21, 65, 0, 61, 11, 55],
    [23, 11, 64, 51, 46, 51, 51, 33, 29, 41, 42, 61, 0, 62, 23],
    [72, 52, 31, 43, 65, 29, 46, 31, 51, 23, 59, 11, 62, 0, 59],
    [46, 21, 51, 64, 23, 59, 33, 37, 11, 37, 61, 55, 23, 59, 0]
]

marque = [False] * len(graph)
longueur = 0
longueurMin = 1000
n = 1  
cycle = []
borne = 400

def dfs( start):
    global n
    global longueur
    global longueurMin
    global source
    global borne

    if start == source and n == len(graph) + 1:
        print('  Tour =', cycle, longueur)
        if longueur <= longueurMin:
            longueurMin = longueur
            borne=longueur
        return
    elif marque[start]:
        return
    else:
        if longueur >= borne:        
            return
       
        marque[start] = True
        cycle.append(start)
        for candidate in range(len(graph[start])):
            if not marque[candidate] or (candidate == source and n == len(graph)):
                longueur += graph[start][candidate]
                n = n + 1
                if longueur <= borne:
                    dfs(candidate)
                longueur = longueur - graph[start][candidate]
                n = n - 1
        marque[start] = False
        cycle.pop(-1)

source = 0
dfs(source)
print('Le meilleur tour =', longueurMin)
