#
#
def isValidSudoku(board):
    # Initialize an empty list to store seen elements in rows, columns, and subgrids.
    r = []

    # Iterate through the Sudoku board.
    for i in range(9):
        for j in range(9):
            ele = board[i][j]
            # Check if the element is not '.' (empty cell).
            if ele != '.':
                # Check for violations in the current row, column, and subgrid.
                r += [(i, ele), (ele, j), (i // 3, j // 3, ele)]
    print(len(r))
    print(len(set(r)))
    for i in r:
        print(i)

print(isValidSudoku([
                     ["8", ".", ".", ".", "5", ".", ".", "1", "."],
                     [".", "4", ".", "3", ".", ".", ".", ".", "."],
                     [".", ".", ".", ".", ".", "3", ".", ".", "1"],
                     ["8", ".", ".", ".", ".", ".", ".", "2", "."],
                     [".", ".", "2", ".", "7", ".", ".", ".", "."],
                     [".", "1", "5", ".", ".", ".", ".", ".", "."],
                     [".", ".", ".", ".", ".", "2", ".", ".", "."],
                     [".", "2", ".", "9", ".", ".", ".", ".", "."],
                     [".", ".", "4", ".", ".", ".", ".", ".", "."]
]))
# def isValidSudoku(board):
#     def is_in_square(row, column, data):
#         nonlocal board
#         check_data = [
#             [(0, 0), (2, 2)],
#             [(0, 3), (2, 5)],
#             [(0, 6), (2, 8)],
#             [(3, 0), (5, 2)],
#             [(3, 3), (5, 5)],
#             [(3, 6), (5, 8)],
#             [(6, 0), (8, 2)],
#             [(6, 3), (8, 5)],
#             [(6, 6), (8, 8)]
#         ]
#         for d in check_data:
#             x, y = d[0], d[1]
#
#             if x[0] <= row <= y[0] and x[1] <= column <= y[1]:
#                 if row == 1 and column == 3:
#                     print(x, y)
#                 return check_square(row, column, data, x, y)
#
#     def check_square(row, column, data, x, y):
#         nonlocal board
#         for i in range(x[0], y[0] + 1):
#             for j in range(x[1], y[1] + 1):
#                 if row == 1 and column == 3:
#                     # print(x, y)
#                     print(f"({i}, {j}) = {board[i][j]}, {data}")
#                 if i == row and j == column:
#                     continue
#                 if board[i][j] == data:
#                     return False
#         return True
#
#     def is_in_rows(row, column, data):
#         nonlocal board
#         for r in range(0, 9):
#             if row == r:
#                 continue
#             if board[r][column] == data:
#                 return False
#         return True
#
#     def is_in_cols(row, column, data):
#         nonlocal board
#         for col in range(0, 9):
#             if col == column:
#                 continue
#             if board[row][col] == data:
#                 return False
#         return True
#
#     data = []
#     for row in range(len(board)):
#         for col in range(len(board[row])):
#             # print(f"({row}, {col}) = {board[row][col]}")
#             # if row == 2 and col == 3:
#             #     print(board[row][col])
#             if board[row][col] == ".":
#                 # print(0)
#                 continue
#             # print(board[row][col])
#
#             data.append(
#                 is_in_square(row, col, board[row][col]) and is_in_rows(row, col, board[row][col]) and is_in_cols(row,
#                                                                                                                  col,
#                                                                                                                  board[
#                                                                                                                      row][
#                                                                                                                      col]))
#     print(data)
#     return all(data)
#
# print(isValidSudoku([
#                      [".", ".", ".", ".", "5", ".", ".", "1", "."],
#                      [".", "4", ".", "3", ".", ".", ".", ".", "."],
#                      [".", ".", ".", ".", ".", "3", ".", ".", "1"],
#                      ["8", ".", ".", ".", ".", ".", ".", "2", "."],
#                      [".", ".", "2", ".", "7", ".", ".", ".", "."],
#                      [".", "1", "5", ".", ".", ".", ".", ".", "."],
#                      [".", ".", ".", ".", ".", "2", ".", ".", "."],
#                      [".", "2", ".", "9", ".", ".", ".", ".", "."],
#                      [".", ".", "4", ".", ".", ".", ".", ".", "."]
# ]))
#
#
#
#
