class DiGraph(object):
    def __init__(self):
        self.nodes = set()
        self.body = dict()
        
    def AddNode(self, node):
        self.nodes.add(node)
        if node not in self.body:
            self.body[node] = []
    
    def AddEdge(self, u, v):
        self.body[u].append(v)
    
    def RemoveNode(self, node):
        self.nodes.remove(node)
        del self.body[node]
        for n in self.nodes:
            idx = 0
            while idx < len(self.body[n]):
                if self.body[n][idx] == node:
                    self.body[n].pop(idx)
                    break
                idx += 1
        

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if numCourses == 0:
            return []
        ans = []
        g = DiGraph()
        for n in range(numCourses):
            g.AddNode(n)
        for vec in prerequisites:
            g.AddEdge(vec[0], vec[1])
        toBeLearned = [n for n in range(numCourses) if len(g.body[n])==0]
        ans = []
        while len(toBeLearned) > 0:
            for n in toBeLearned:
                ans.append(n)
                g.RemoveNode(n)
            toBeLearned = [n for n in g.body if len(g.body[n])==0]
        if len(g.body) == 0:
            return ans
        else:
            return []
                