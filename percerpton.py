"""
Write a function which returns two lists A and B such that there are each list
contains 100 points which lie on either side of a line ax + by + c = 0. Each
list should contain 100 points.
a, b, c are the arguments to the function.
"""

import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_data(a, b, c):
    """
    This function returns two lists A and B of 100 points each which lie on
    opposite sides of the line ax + by + c = 0.
    The points A are labeled -1 and points B are labeled +1.
    """
    A = []
    B = []
    # Add points till we have 100 points in each list.
    while len(A)<100 or len(B)<100:
        x = random.uniform(-100, 100)
        y = random.uniform(-100, 100)
        if a*x + b*y + c > 0:
            # Append a list 1, x, y to the list.
            B.append(np.array([1, x, y]))
        elif a*x + b*y + c < 0:
            # Append a list 1, x, y to the list.
            A.append(np.array([1, x, y]))
    return A, B

# Generate training data
A, B = generate_data(2, 3, 4)
########################### Synthetic Data Generated ###########################

# Algorithm begins here.

"""
Write a function which checks if a given point is correctly classified by a
given weight vector or not.
The arguments to the function should be weight vector, point and its label.
"""
def check_classification(w, x, y):
    """This function checks if a given points is correctly classified by a
    given weight vector or not.
    """
    # If the point is correctly classified, return True.
    if np.dot(w, x)*y > 0:
        return True
    else:
        return False


def plot_data(A, B, w):
    """This function plots the data points and the line ax + by + c = 0.
    """
    # Plot the points in the list A.
    for x in A:
        plt.plot(x[1], x[2], 'ro')
    # Plot the points in the list B.
    for x in B:
        plt.plot(x[1], x[2], 'bo')
    # Plot the line ax + by + c = 0.
    x = np.linspace(-100, 100, 100)
    y = (-w[0] - w[1]*x)/w[2]
    plt.plot(x, y, 'g-')
    plt.show()
    # Close the plot
    plt.close()

"""
Write a function which returns a weight vector which correctly classifies all
the points in the given list.
"""
def perceptron(A, B):
    """
    This function iterates through all the points in the lists and adjusts the
    weights till all the points are correctly classified.
    """
    # Initialize the weight vector to zero.
    w = np.array([0, 0, 0])
    # Initialize the number of iterations to zero.
    iterations = 0
    # Initialize the number of misclassified points to 200.
    misclassified = 200
    # Iterate till all the points are correctly classified.
    while misclassified > 0:
        # Initialize the number of misclassified points to zero.
        misclassified = 0
        # Iterate through all the points in the list A.
        for x in A:
            # If the point is misclassified, update the weight vector.
            if check_classification(w, x, -1) == False:
                w = w - x
                misclassified += 1
        # Iterate through all the points in the list B.
        for x in B:
            # If the point is misclassified, update the weight vector.
            if check_classification(w, x, 1) == False:
                w = w + x
                misclassified += 1
        iterations += 1
    # Return the weight vector.
    return w

# Call the perceptron function.
w = perceptron(A, B)
# Plot the line ax + by + c = 0 and the points in the lists A and B.
plot_data(A, B, np.array([4, 2, 3]))
# Plot the data points and the line ax + by + c = 0.
plot_data(A, B, w)

