class Solution:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """

        def theSpauseof(num):
            if num % 2 == 0:
                return num + 1
            else:
                return num - 1

        num2seat = {j: i for i, j in enumerate(row)}
        moves = 0
        for i in range(0, len(row), 2):
            spause = theSpauseof(row[i])
            if row[i + 1] != spause:
                spause_seat = num2seat[spause]
                num2seat[spause] = i + 1
                num2seat[row[i + 1]] = spause_seat
                row[i + 1], row[spause_seat] = row[spause_seat], row[i + 1]
                moves += 1
        return moves