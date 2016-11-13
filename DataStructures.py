import numpy as np


class NetworkGraph:
    matrix = None
    V = None

    def __init__(self, V, default_values = 0):
        self.matrix = default_values*np.ones((V+2,V+2)) # Add 2 for s and t nodes
        self.V = V+2
        self.s, self.t = 0, V+1

    # Sets the weight of an edge
    #   @edge is a tuple (u,v)
    #   @weight is the desired weight to set
    def add_edge(self, edge, weight):
        assert type(edge) is tuple and len(edge) == 2, 'Invalid edge: {}. Edge must be a tuple of form (u,v)'.format(edge)
        u,v = edge
        assert u < self.V and v < self.V, 'Invalid edge: {} for graph with {} vertices'.format(edge, self.V)
        self.matrix[u,v] = weight

    # Returns all edges of the form (v, .)
    def get_out_edges(self, v):
        assert v < self.V, 'Invalid vertex: {} for graph with {} vertices'.format(v, self.V)
        return self.matrix[v,:]

    # Returns all edges of the form (.,v)
    def get_in_edges(self, v):
        assert v < self.V, 'Invalid vertex: {} for graph with {} vertices'.format(v, self.V)
        return self.matrix[:,v]

    def get_edges(self):
        return np.argwhere(self.matrix > 0)

    def flatten_matrix(self):
        return self.matrix.reshape((self.matrix.shape[0] * self.matrix.shape[1],))