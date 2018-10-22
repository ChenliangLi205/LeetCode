import time

B = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

B1 = [[".","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]


def solution(board):
    blanks = []
    row_sets, col_sets = [set() for _ in range(9)], [set() for _ in range(9)]
    block_sets = [[set() for _ in range(3)] for __ in range(3)]
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                blanks.append((i, j))
            else:
                row_sets[i].add(board[i][j])
                col_sets[j].add(board[i][j])
                block_sets[i//3][j//3].add(board[i][j])

    def is_solution(b):
        loc = None
        for i in range(9):
            for j in range(9):
                if b[i][j] == ".":
                    loc = (i, j)
                    break
        if loc is None:
            return True
        else:
            for i in range(1, 10):
                n = str(i)
                if is_valid(n, loc[0], loc[1]):
                    b[loc[0]][loc[1]] = n
                    row_sets[loc[0]].add(n)
                    col_sets[loc[1]].add(n)
                    block_sets[loc[0]//3][loc[1]//3].add(n)
                    if is_solution(b):
                        return True
                    b[loc[0]][loc[1]] = "."
                    row_sets[loc[0]].remove(n)
                    col_sets[loc[1]].remove(n)
                    block_sets[loc[0]//3][loc[1]//3].remove(n)
            return False

    def is_valid(num, i, j):
        return num not in row_sets[i] and num not in col_sets[j] and num not in block_sets[i // 3][j // 3]

    is_solution(board)
    return

if __name__ == '__main__':
    t1 = time.time()
    solution(B)
    for i in range(len(B)):
        print(B[i])

    print(time.time()-t1)
    # new_b = [[0] * 9 for _ in range(9)]
    # for i in range(len(board2)):
    #     for j in range(len(board2[i])):
    #         if board2[i][j] != ".":
    #             new_b[i][j] = int(board2[i][j])
    # print(find_num(new_b, 0, 0))
