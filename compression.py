
"""
Write a function to generate a random binary string of length 1000000.
The function should take the argument p which is the probability of a bit being
0.
"""

import random

def random_binary_string(p):
    """
    This function takes a probability p and returns a random binary string of
    length 1000000.

    :p: probability of a bit being 0
    :returns: a random binary string of length 1000000

    """
    random_string = []
    for i in range(1000000):
        # Generate a random number between 0 and 1
        random_number = random.random()
        # If the number is less than p, append 0 to the list
        if random_number < p:
            random_string.append('0')
        # Else append 1 to the list
        else:
            random_string.append('1')
    return ''.join(random_string)

def compress(string):
    """This function takes a string and compresses.

    :string: Binary string to be compressed
    :returns: Compressed list

    """
    compressed_string = []
    # Append the first bit
    compressed_string.append(string[0])
    # Count the number of consecutive 0s and 1s
    count = 1
    for i in range(1, len(string)):
        # If consecutive bits are same, count them
        if string[i] == string[i - 1]:
            count += 1
        # If the next bit is different, append the count to the list and reset it
        else:
            compressed_string.append(str(count))
            count = 1

    # Append the last count to the list
    compressed_string.append(str(count))
    return compressed_string


# We can judge how much compression took place by looking at the length of the
# compressed string.
def plot_p_vs_compression():
    """This function plots a graph of probability of occurrence of 0 vs the
    length of the compressed string.
    Probability should be on the x axis and the length should be on y axis.
    """
    import matplotlib.pyplot as plt
    # Create a list of probabilities
    probabilities = [i / 1000 for i in range(1001)]
    # Create a list of lengths of compressed strings
    lengths = []
    for p in probabilities:
        string = random_binary_string(p)
        compressed_string = compress(string)
        lengths.append(len(compressed_string))
    plt.plot(probabilities, lengths)
    plt.xlabel('Probability of occurrence of 0')
    plt.ylabel('Length of compressed string')
    plt.show()

def main():
    """Main function"""
    plot_p_vs_compression()

if __name__ == '__main__':
    main()

