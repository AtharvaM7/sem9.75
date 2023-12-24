"""
Write a function which creates a random directed graph with n nodes and m edges.
"""
import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import math

def create_graph(n, m):
    """
    Creates a random directed graph of n nodes and m edges.
    """
    # Create a graph
    G = nx.DiGraph()
    # Add nodes
    G.add_nodes_from(range(n))
    # Add edges
    for i in range(m):
        # Pick a random source and target
        source = random.randint(0, n - 1)
        target = random.randint(0, n - 1)
        # Add the edge
        G.add_edge(source, target)
    return G

def pagerank_random_walk(G):
    """
    Finds the pagerank of a graph using random walks and returns it as a
    dictionary.
    """
    # Create a dictionary
    pagerank = {}
    # Set all nodes to have a pagerank of 0
    for node in G.nodes():
        pagerank[node] = 0
    # Pick a random node to start at
    current_node = random.choice(list(G.nodes()))
    # Do n random walks
    n = 10000000
    for i in range(n):
        # Add 1 to the pagerank of the current node
        pagerank[current_node] += 1
        # Get a list of current nodes neighbors.
        neighbors = list(G.neighbors(current_node))
        # If the current node has no neighbors, pick a random node to start at
        if len(neighbors) == 0:
            current_node = random.choice(list(G.nodes()))
        # Otherwise, pick a random neighbor to move to
        else:
            current_node = random.choice(neighbors)
    # Normalize the pagerank
    for node in pagerank:
        pagerank[node] /= n
    return pagerank

def pagerank_points_distribution(G):
    """
    Finds the pagerank of a graph using points distribution and returns it as a
    dictionary.
    """
    # Create a dictionary
    pagerank = {}
    # Get number of nodes.
    n = len(G.nodes())
    # Set all nodes to have a pagerank of 1/n
    for node in G.nodes():
        pagerank[node] = 1 / n
    # Start iterating
    p = 100000000
    for i in range(p):
        # Create a new dictionary.
        new_pagerank = {}
        # Set all nodes to have a pagerank of 0
        for node in G.nodes():
            new_pagerank[node] = 0
        # Iterate through all nodes
        for node in G.nodes():
            # Get the list of neighbors
            neighbors = list(G.neighbors(node))
            # If the list has no neighbors then distribute the points to all
            # the nodes equally.
            if len(neighbors) == 0:
                for node in G.nodes():
                    new_pagerank[node] += pagerank[node] / n
            # Otherwise, distribute the points to all the neighbors equally.
            else:
                for neighbor in neighbors:
                    new_pagerank[neighbor] += pagerank[node] / len(neighbors)
        # Set the pagerank to the new pagerank
        pagerank = new_pagerank
    return pagerank

# Test the function
G = create_graph(10, 20)
pagerank = pagerank_points_distribution(G)
# Verify using networkx
pagerank_nx = nx.pagerank(G)
# Sort the dictionaries and create lists of the nodes.
# The list should only contain node numbers.
pagerank = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)
pagerank = [x[0] for x in pagerank]
pagerank_nx = sorted(pagerank_nx.items(), key=lambda x: x[1], reverse=True)
pagerank_nx = [x[0] for x in pagerank_nx]
# Print the results
print(pagerank)
print(pagerank_nx)





