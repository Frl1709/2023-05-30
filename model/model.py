import copy
import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self.listTeams = []
        self.listYear = []

        self.grafo = nx.Graph()
        self.nodes = []
        self.edges = []
        self.edgePesati = []

        self.loadTeams()

    def getDetails(self, v0):
        tmp = []
        for e in self.edgePesati:
            if e[0] == v0:
                tmp.append((e[0], e[1], e[2]))
            if e[1] == v0:
                tmp.append((e[1], e[0], e[2]))

        tmp = sorted(tmp, key=lambda x: x[2], reverse=True)
        return tmp


    def loadTeams(self):
        self.listTeams = DAO.getTeams()

    def buildGraph(self, nome):
        self.grafo.clear()
        self.nodes.clear()
        self.edges.clear()
        self.nodes = DAO.getNodes(nome)
        self.grafo.add_nodes_from(self.nodes)

        for n in self.nodes:
            self.listYear.append(n)

        connection = DAO.getEdge(nome)
        for i in range(len(self.nodes)):
            for j in range(i+1, len(self.nodes)):
                if not self.grafo.has_edge(self.nodes[i], self.nodes[j]):
                    self.grafo.add_edge(self.nodes[i], self.nodes[j])
                    self.edges.append((self.nodes[i], self.nodes[j]))

        for v1, v2, w in connection:
            self.grafo[v1][v2]['weight'] = w
            self.edgePesati.append((v1, v2, w))

    def getGraphSize(self):
        return len(self.nodes), len(self.edges)
