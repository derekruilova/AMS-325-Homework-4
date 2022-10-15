import numpy as np
import numpy.linalg as linalg

def markov_chain(n, N):

    p = np.random.random(n)
    p /= p.sum()
#Making a n-vector with random values whos sum is 1
    M = np.random.rand(n,n)
    r = M.sum(axis=1)[:,None]
    P = M / r
#Makes a nxn matrix with rows that add up to 1
    transposed_P = P.T
#Making a variable for the tranpose of P

    for i in range(N):
        p = p * transposed_P
#Takes p original and renames it to the product of p and P.T for N times
    eigenValues, eigenVectors = linalg.eig(P.T)
    idx = eigenValues.argsort()[::-1]
    eigenValues = eigenValues[idx]
    eigenVectors = eigenVectors[:, idx]
#This section here creates the eigenvalues and vectors. It also puts them in order so I can call the highest value as the [0] index
    p_stationary = eigenVectors[0]
    p_stationary /= sum(p_stationary)
#P_stationary just computed based off the intructions in the pdf. It should also add up to 1.
    norm_p = [0] * N
    for i in range(N):
        p = p - p_stationary
        norm_p[i] = np.linalg.norm(p)

    return norm_p
#Subsection 5 of the assignment was the part where I got troubled. This code is experimental and was done to the best of my understanding

    """
    This function calculates the markov chain
    - n serves as the parameters for the nxn matrix which in this question becomes a 5x5
    - N serves as the parameter for the number of steps that p was to be multiplied by transpose P and saved as the new p value
        """
print(markov_chain(5, 50))
