# def add(x, y, z=0):
#     return x + y+z
#
#
# print(add(4, 6))
# print(add(2, 4, 6))

def add_two_matrices():
    mat1 = [[11, 25, 32],
            [14, 55, 26],
            [72, 83, 39]]

    mat2 = [[49, 68, 27],
            [16, 65, 24],
            [53, 22, 41]]

    mat3 = [[0, 0, 0] for _ in range(len(mat1))]

    for row in mat1:
        string = ' '.join(map(str, row))
        print(string)
    print()

    for row in mat2:
        string = ' '.join(map(str, row))
        print(string)
    print()

    for i in range(len(mat1)):
        for j in range(len(mat1[i])):
            mat3[i][j] = mat1[i][j] + mat2[i][j]

    for row in mat3:
        new = ' '.join(map(str, row))
        print(new)


add_two_matrices()

# mat2 = [[9, 8, 7],
#         [6, 5, 4],
#         [3, 2, 1]]
#
# for row in mat2:
#     # Use the 'join' method to convert the row elements to strings and concatenate them with spaces
#     row_str = ' '.join(map(str, row))
#     print(row_str)


# mat2 = [[9, 8, 7],
#         [6, 5, 4],
#         [3, 2, 1]]
#
# for row in mat2:
#     row_str = ' '.join(str(elem) for elem in row)
#     print(row_str)
