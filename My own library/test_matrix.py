from custom_math_lib.matrix import matrix_addition

def test_matrix_addition():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    assert matrix_addition(A, B) == [[6, 8], [10, 12]]
