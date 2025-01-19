def matrix_addition(A, B):
    """Adds two matrices element-wise."""
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must be the same size")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_multiplication(A, B):
    """Multiplies two matrices."""
    if len(A[0]) != len(B):
        raise ValueError("Invalid matrix dimensions for multiplication")
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
