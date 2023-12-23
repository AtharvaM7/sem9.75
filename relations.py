import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

"""
Write a function which creates a graph of n nodes.
"""
def create_graph(n):
    """
    Creates a graph of n nodes with edge weights 1 or -1 with equal probability.
    """
    G = nx.Graph()
    G.add_nodes_from(range(n))
    # Add all possible edges with weight 1 or -1 with equal probability
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < 0.5:
                G.add_edge(i, j, weight=1)
            else:
                G.add_edge(i, j, weight=-1)
    return G

"""
Write a function which displays the graph. The weights of edges should also be
displayed.
"""
def display_graph(G):
    """
    Displays the graph G.
    """
    # Get the positions of the nodes
    pos = nx.spring_layout(G)
    # Get the weights of the edges
    edge_labels = nx.get_edge_attributes(G, 'weight')
    # Draw the graph
    nx.draw(G, pos, with_labels=True)
    # Draw the edge labels
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    # Show the graph
    plt.show()


"""
Write a function which returns a list of all possible triangles in the graph.
"""
def get_triangles(G):
    """
    Returns list of all possible triangles in the graph G.
    """
    # Create list of triangles
    triangles = []
    # Get all possible triangles
    # Iterate from 0 to n-2
    for i in range(len(G.nodes)-2):
        # Iterate from i+1 to n-1
        for j in range(i+1, len(G.nodes)-1):
            # Iterate from j+1 to n
            for k in range(j+1, len(G.nodes)):
                # Check if triangle exists
                if G.has_edge(i, j) and G.has_edge(j, k) and G.has_edge(k, i):
                    triangles.append([i, j, k])
    return triangles

"""
Write a function to check if a triangle formed by nodes (i,j,k) is stable or
not.
The argument of the function is a list of three nodes [i,j,k].
"""
def is_stable(triangle):
    """
    Checks if the triangle is stable or not.
    """
    # Get the nodes
    i, j, k = triangle
    # Get the edges of the triangle and their weights.
    edge1 = G.get_edge_data(i, j)['weight']
    edge2 = G.get_edge_data(j, k)['weight']
    edge3 = G.get_edge_data(k, i)['weight']
    list_edges = [edge1, edge2, edge3]
    # Check if the triangle is stable
    # Check if all edges are +1
    if list_edges.count(1) == 3:
        return True
    # Check if 1 edge is +1 and 2 edges are -1
    elif list_edges.count(1) == 1 and list_edges.count(-1) == 2:
        return True
    # For the remaining cases, the triangle is not stable
    else:
        return False

"""
Write a function which finds the total number of unstable triangles in a graph.
"""
def num_unstable_triangles(G):
    """
    Returns number of unstable triangles in a graph.
    """
    num = 0
    # Get all possible triangles
    triangles = get_triangles(G)
    # Iterate through all triangles
    for triangle in triangles:
        # Check if triangle is unstable
        if not is_stable(triangle):
            num += 1
    return num

"""
Write a function which makes a triangle stable.
"""
def make_stable(G, triangle):
    """
    Modifies G such that a triangle becomes stable.
    The assumption is that the triangle is unstable.
    """
    # Get the nodes
    i, j, k = triangle
    # Get the edges of the triangle and their weights.
    edge1 = G.get_edge_data(i, j)['weight']
    edge2 = G.get_edge_data(j, k)['weight']
    edge3 = G.get_edge_data(k, i)['weight']
    list_edges = [edge1, edge2, edge3]
    # If all the weights are -1 then make any edge +1
    if list_edges.count(-1) == 3:
        # Get a random edge and make it +1
        edge = random.choice([edge1, edge2, edge3])
        if edge == edge1:
            G[i][j]['weight'] = 1
        elif edge == edge2:
            G[j][k]['weight'] = 1
        else:
            G[k][i]['weight'] = 1
    # If two edges are 1 and one is -1, then either make all edges +1 or make
    # one of the +1 edges -1
    elif list_edges.count(1) == 2 and list_edges.count(-1) == 1:
        # Choose a random edge and change its sign.
        edge = random.choice([edge1, edge2, edge3])
        if edge == edge1:
            G[i][j]['weight'] = -1
        elif edge == edge2:
            G[j][k]['weight'] = -1
        else:
            G[k][i]['weight'] = -1
    # Return the modified graph
    return G

"""
Write a function which stabilizes all triangles in the graph.
"""
def stabilize(G):
    """
    Takes an unstable graph and returns a stable graph.
    """
    while num_unstable_triangles(G) != 0:
        # Get all triangles
        triangles = get_triangles(G)
        # Choose a random triangle
        triangle = random.choice(triangles)
        # Check if triangle is unstable
        if not is_stable(triangle):
            # Make the triangle stable
            G = make_stable(G, triangle)
    return G

"""
Write a function which checks if a graph is stable or not.
"""
def is_stable_graph(G):
    """
    Checks if the entire graph is stable.
    """
    # Get triangles.
    triangles = get_triangles(G)
    # Iterate through all triangles
    for triangle in triangles:
        # Check if triangle is unstable
        if not is_stable(triangle):
            return False
    return True

"""
Write a function which gives a list of nodes which fall in two coalitions.
"""
def find_coalitions(G):
    """
    Returns two coalitions of the graph.
    """
    # Pick a random node
    node = random.choice(list(G.nodes))
    # Get the neighbors of the node with weight 1
    neighbors = [n for n in G.neighbors(node) if G[node][n]['weight'] == 1]
    neighbors.append(node)
    # Get the neighbors of the node with weight -1
    neighbors_neg = [n for n in G.neighbors(node) if G[node][n]['weight'] == -1]
    # Return the lists of nodes
    coalitions = [neighbors, neighbors_neg]
    return coalitions

G = create_graph(8)
G = stabilize(G)
display_graph(G)
print(is_stable_graph(G))
print(find_coalitions(G))


