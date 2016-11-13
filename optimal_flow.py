import numpy as np
from scipy import optimize
from DataStructures import NetworkGraph


def solve_optimal(payments_list):
    """
    Takes in a list of Payments and finds the optimal flow values
    from country to country.
    :param payments_list: list of Payments given from the Backend
    :return:              a list of flow values for each edge from country to country
    """
    capacity_graph, cost_graph = initialize(payments_list)
    min_weights, constraint_matrix, constraint_res = formulate_simplex(capacity_graph, cost_graph)
    flow_vals = run_simplex(min_weights, constraint_matrix, constraint_res)
    return flow_vals


def initialize(payments_list):
    """
    Takes in a list of Payments and constructs two NetworkGraph objects
    that represent a graph whose edge weights are capacities and another
    graph whose edge weights are cut percentages.
    :param payments_list: list of Payments given from the Backend
    :return:              two Graph objects
    """
    # TODO: Implement this method
    return NetworkGraph(1), NetworkGraph(1)


def formulate_simplex(capacity_graph, cost_graph):
    """
    Takes in a capacity graph and cost graph in order to output
    c, A, b such that we form inputs readable by Simplex.
    :param capacity_graph: the graph holding edge weights as capacities.
    :param cost_graph:     the graph holding edge weights as cut percentages.
    :return:               parameters for simplex to function.
    """
    # TODO: Implement this method
    min_weights = np.zeros(4)
    constraint_matrix = np.zeros(4)
    constraint_res = np.zeros(4)
    return min_weights, constraint_matrix, constraint_res


def run_simplex(c, A_equality, b_equality):
    return optimize.linprog(c, A_eq=A_equality, b_eq=b_equality)

