class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return True
        if len(board) == 0:
            return False
        if len(board[0]) == 0:
            return False

        rows, cols = len(board), len(board[0])
        if rows * cols < len(word):
            return False
        letter2loc = dict()
        for i in range(rows):
            for j in range(cols):
                char = board[i][j]
                if char not in letter2loc:
                    letter2loc[char] = [(i, j)]
                else:
                    letter2loc[char].append((i, j))
        for char in word:
            if char not in letter2loc:
                return False
        stack = [(0, *n) for n in letter2loc[word[0]]]
        visited = []

        while len(stack):
            length, r, c = stack.pop()
            if length == len(word) - 1:
                return True
            target = word[length+1]
            visited = visited[:length]
            visited.append((r,c))
            if r - 1 >= 0:
                if board[r - 1][c] == target and (r - 1, c) not in visited:
                    stack.append((length + 1, r - 1, c))
            if c - 1 >= 0:
                if board[r][c - 1] == target and (r, c - 1) not in visited:
                    stack.append((length + 1, r, c - 1))
            if r + 1 < rows:
                if board[r + 1][c] == target and (r + 1, c) not in visited:
                    stack.append((length + 1, r + 1, c))
            if c + 1 < cols:
                if board[r][c + 1] == target and (r, c + 1) not in visited:
                    stack.append((length + 1, r, c + 1))
        return False