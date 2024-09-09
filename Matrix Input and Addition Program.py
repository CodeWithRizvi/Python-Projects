# Function to create a matrix of size m x n with user input
def matrix(m, n):
    o = []  # Initialize an empty list to store the matrix
    for i in range(m):  # Loop through each row (m times)
        row = []  # Initialize an empty list for the current row
        for j in range(n):  # Loop through each column (n times)
            inp = int(input(f"Enter element at position [{i}][{j}]: "))  # Get user input for each element
            row.append(inp)  # Add the element to the current row
        o.append(row)  # Append the completed row to the matrix
    return o  # Return the matrix

# Function to sum two matrices A and B
def sum(A, B):
    output = []  # Initialize an empty list to store the result matrix
    for i in range(len(A)):  # Loop through each row of matrix A (or B, since they have the same size)
        row = []  # Initialize an empty list for the current row of the result matrix
        for j in range(len(A[0])):  # Loop through each column in the current row
            row.append(A[i][j] + B[i][j])  # Add corresponding elements from A and B and append to the row
        output.append(row)  # Append the completed row to the result matrix
    return output  # Return the result matrix

# Get matrix dimensions m (number of rows) and n (number of columns) from the user
m = int(input("Enter the number of rows (m):\n"))
n = int(input("Enter the number of columns (n):\n"))

# Input matrix A
print("Enter Matrix A")
A = matrix(m, n)  # Call the matrix function to get matrix A
print("Matrix A:", A)  # Display matrix A

# Input matrix B
print("Enter Matrix B")
B = matrix(m, n)  # Call the matrix function to get matrix B
print("Matrix B:", B)  # Display matrix B

# Compute the sum of matrix A and B
s = sum(A, B)  # Call the sum function to get the matrix sum of A and B
print("Sum of A and B:", s)  # Display the resulting sum matrix
