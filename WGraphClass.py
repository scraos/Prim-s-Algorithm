def edges_to_set(edges):
    nods = []
    for i in edges:
        if i[0] not in nods:
            nods.append(i[0])
        if i[1] not in nods:
            nods.append(i[1])
    return nods

class Dgraph():
    def __init__(self):
        self.nodes = []
        self.arrows = []
        self.dists = {}

    def addnode(self,n):
        self.nodes.append(n)

    def addarrow(self,arrow,dist):
        self.arrows.append(arrow)
        self.dists[arrow] = dist

    def neighbors_of(self,node):
        set1 = []
        for i in self.arrows:
            if i[1] == node:
                set1.append(i[0])
            elif i[0] == node:
                set1.append(i[1])
        return set1

    def getLength(self, node1, node2):
        if (node1, node2) in self.arrows:
            return self.dists[(node1, node2)]
        elif (node2, node1) in self.arrows:
            return self.dists[(node2, node1)]

    def closest_neighb(self, node):
        mindist = 10e3
        close_neighb = None
        for i in self.arrows:
            curdist = self.getLength(i[0],i[1])
            if i[1] == node and curdist < mindist:
                mindist = curdist
                close_neighb = i[0]
            elif i[0] == node and curdist < mindist:
                mindist = curdist
                close_neighb = i[1]
        return [close_neighb, mindist]

    def get_edges(self,arrowlist):
        near_edges = []
        searchlist = set(self.arrows)-set(arrowlist)
        nodes1 = edges_to_set(arrowlist)
        deletelist = []
        for k in searchlist:
            if (k[1] in nodes1) and (k[0] in nodes1):
                deletelist.append(k)
        searchlist = searchlist - set(deletelist)
        for i in searchlist:
            for j in arrowlist:
                if (i[0] == j[0]) or (i[0] == j[1]) or (i[1] == j[0]) or (i[1] == j[1]):
                    near_edges.append(i)
        return near_edges