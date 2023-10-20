'''Write a code to compress a given image using SVD.
This program takes an image in the same directory. 
Converts it into grayscale.
Converts it into square matrix.
Factorizes the matrix into U, S, V.
Reconstructs the matrix using U, S, V.
Plots the original and reconstructed image.
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# Function to convert image to grayscale
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

# Crop the image to make it square
def crop(img):
    x, y = img.shape
    if x > y:
        img = img[:y, :]
    elif y > x:
        img = img[:, :x]
    return img

# Factorize the matrix into U, S, V
def svd(img):
    U, S, V = np.linalg.svd(img)
    return U, S, V

# Keep only the first k singular values and discard the rest
def truncate(U, S, V, k):
    U = U[:, :k]
    S = S[:k]
    V = V[:k, :]
    return U, S, V

# Reconstruct the matrix using U, S, V
def reconstruct(U, S, V):
    return np.dot(U * S, V)

# Plot the original and reconstructed image
def plot(img, img_reconstructed):
    plt.subplot(121)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.subplot(122)
    plt.imshow(img_reconstructed, cmap='gray')
    plt.title('Reconstructed Image')
    plt.show()

# Main function
def main():
    # Read the image
    img = mpimg.imread('image.jpg')
    # Convert image to grayscale
    img = rgb2gray(img)
    # Crop the image to make it square
    img = crop(img)
    # Print the size of image
    print('Size of image: ', img.shape)
    # Factorize the matrix into U, S, V
    U, S, V = svd(img)
    # Keep only the first k singular values and discard the rest
    # Take the input of k from the user
    k = int(input('Enter the value of k: '))
    U, S, V = truncate(U, S, V, k)
    # Reconstruct the matrix using U, S, V
    img_reconstructed = reconstruct(U, S, V)
    # Plot the original and reconstructed image
    plot(img, img_reconstructed)

if __name__ == '__main__':
    main()


