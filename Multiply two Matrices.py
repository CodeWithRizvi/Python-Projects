A = [[1,3,5],
    [2,6,8],
    [4,2,4]]
B = [[1,2,5],
    [2,2,8],
    [4,2,4]]
C = [[0,0,0],
    [0,0,0],
    [0,0,0]]
# Perform matrix multiplication
# Outer loop iterates through rows of matrix C (and A)
for i in range(0,len(C)):
    # Middle loop iterates through columns of matrix C (and B)
    for j in range(0,len(C)):
        # Inner loop calculates the dot product of row from A and column from B
        for k in range(0,len(C)):
            # Accumulate the product of corresponding elements in A's row and B's column
            C[i][j]+= A[i][k]*B[k][j]

# Print the resulting matrix C row by row
for row in C:
    print(row)