#!/usr/bin/python3
""" 1. Divide a matrix - 2-matrix_divided.py """


def matrix_divided(matrix, div):
    """
    This function that divides all elements of a matrix
    rounded to 2 decimal places

    Args:
        matrix: the matrix
        div: number by which to divide

    Raises:
        TypeError if matrix is not list of ints or floats
        TypeError if each row is not same size
        TypeError if div is not a number
        ZeroDivisionError if div is 0

    Return:
        A new matrix
    """

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")

    new_matrix = [x[:] for x in matrix]

    row_len = len(matrix[0])
    new_element = 0
    for row in range(len(matrix)):
        if(len(matrix[row]) != row_len):
            raise TypeError("Each row of the matrix must have the same size")
        for col in range(len(matrix[row])):
            if type(matrix[row][col]) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)" +
                                " of integers/floats")
            else:
                new_element = (matrix[row][col]) / div
                new_element = round(new_element, 2)
                new_matrix[row][col] = new_element
    return new_matrix
