# AMS-325-Homework-4

This project is comprised of 2 seperate mini projects. We were tasked with solving a mandelbrot problem for the first part and a markov chain for the second part. Both files use libraries such as Numpy and matplotlib. 

For the first problem the task was to compute a mandelbrot set. The problem was as follows:

The Mandelbrot set is the set of complex numbers c for which the function fc(z) = z
2+c does not diverge
when iterated from z = 0. In other words, the sequence fc(0), fc(fc(0)), etc. remains bounded in absolute
value. In this task, you will write a Python script mandelbrot.py to compute the Mandelbrot fractal with the
following Mandelbrot iteration on each point

To solve this I created arrays and a meshgrid to serve as a foundation to the function. One done I made a simple for loop to fill in the grid with calculations done for each iteration of the for loop so that it could fill in the matrix to variable mask. Once completed the matplotlib library was utilized to plot the figure and save it to a seperate png file. 

For the second problem the task was to compute a markov set. The problem was as follows: 

The following diagram depicts a set of states and the transition between each pair of states, where pi denotes
the probability within the ith state and Pij is the probability for state i to transition into state j.
Mathematically, we can represent the diagram with a vector p and a matrix P. The vector p of size n
would describe the probability distribution on n states, with
0 ≤ p[i] ≤ 1 and Xip[i] = 1.
Matrix P is a Markov chain transition matrix of size n × n, where
0 ≤ P[i, j] ≤ 1,
with the sum of each row equal to 1 (i.e., Pj P[i, j] = 1 for all i). Given an old state pold, the new state is
then given by PT pold

To solve this problem I had to create several components including a random number generated vector and matrix whos row(s) would only add up to 1 and for each individual element to be a non negative integer. The following portion of the code involves tranposes and more for loops to find eigen values and vectors and choose the highest value eigenvector. Once that was done I ran into trouble and wasnt sure what to do or how to close off the question which is reflected in the last portion of my code. 
