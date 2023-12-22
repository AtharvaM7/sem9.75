import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import math

def create_graph(n):
    """
    Creates a completely disconnected graph of n nodes.
    """
    G = nx.Graph()
    G.add_nodes_from(range(n))
    return G

def add_random_edge(G):
    """
    Adds a random edge to graph G
    """
    n = len(G.nodes())
    i = random.randint(0, n-1)
    j = random.randint(0, n-1)
    if i != j:
        G.add_edge(i, j)
    return G

def main():
    # Create a disconnected graph of 5000 nodes
    G = create_graph(1000)
    # Create lists to store the number of edges and size of the largest
    # component
    num_edges = []
    largest_component = []
    # Add random edges till the graph is connected
    while nx.is_connected(G) == False:
        G = add_random_edge(G)
        num_edges.append(len(G.edges()))
        largest_component.append(len(max(nx.connected_components(G), key=len)))

    # Plot the number of edges vs size of the largest component
    plt.plot(num_edges, largest_component)
    plt.xlabel("Number of edges")
    plt.ylabel("Size of largest component")
    plt.show()

if __name__ == "__main__":
    main()

