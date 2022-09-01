from abc import abstractmethod, ABC, abstractclassmethod

class DSU:
    def __init__(self, size : int):
        self.parent = [-1] * size
        self.n = size

    def findSet(self, node : int) -> int:
        '''Returns the representative node for the connected component the node
            `node` belongs to.    
        '''
        if self.parent[node] < 0:
            return node
        self.parent[node] = self.findSet(self.parent[node])
        return self.parent[node]

    def unionSet(self, u : int, v : int) -> bool:
        '''
        Tries to merge the components of u and v.
        If components are already in the same component returns False.
        Otherwise, return True 
        '''
        pu, pv = self.findSet(u), self.findSet(v)
        if pu == pv: return False

        size_u, size_v = -self.parent[pu], -self.parent[pv]
        if size_u < size_v:
            size_u, size_v = size_v, size_u
            pu, pv = pv, pu

        self.parent[pu] -= size_v
        self.parent[pv] = pu

        return True

    def componentSize(self, u : int) -> int:
        '''
        Returns the size of the component node `u` belongs to.
        '''
        return -self.parent[self.findSet(u)]


if __name__ == '__main__':
    pass