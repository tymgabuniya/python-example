# python-example

This example uses the Woodbury formula to compute inverse of a matrix. If the matrix has a special structure, the Woodbury formula provides with a more efficient way to compute its inverse.

To be more specific, let N-by-N matrix R can be written as:

R = B Omega B' +D,

with D being a diagonal matrix, Omega is k-by-k and k is much smaller than N.

The Woodbury formula implies that the inverse of R can be written as:

inv(R) = inv(D) - inv(D) B inv(inv(Omega) + B' inv(D) B) B' inv(D).

From the above formula, the efficiency is due to the fact that D is a diagonal matrix and k is much smaller than N.
