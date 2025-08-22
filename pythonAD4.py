#Matrix Multiplication via List Comprehensions

#Write a Python function that performs matrix multiplication using list comprehensions.
# Define a function to perform matrix multiplication of matrices A and B
def matrix_multiplication(A, B):
    """
    Perform matrix multiplication of matrices A and B.

    Args:
    A: First matrix (list of lists).
    B: Second matrix (list of lists).

    Returns:
    Result of matrix multiplication (list of lists).
    """
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must equal number of rows in B")

    # Number of rows and columns in resulting matrix
    num_rows_A = len(A)
    num_cols_B = len(B[0])

    # Perform matrix multiplication using list comprehension
    result = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(num_cols_B)] for i in range(num_rows_A)]

    return result

# Example usage:
if __name__ == "__main__":
    # Example matrices A and B
    A = [[1, 2, 3],
         [4, 5, 6]]

    B = [[7, 8],
         [9, 10],
         [11, 12]]

    # Print the result of matrix multiplication
    print(matrix_multiplication(A, B))

