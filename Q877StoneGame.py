class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        score_Alex, score_Lee = 0, 0
        left, right = 0, len(piles)-1
        turns = 0
        while left < right:
            gain_first = piles[left] - max(piles[left+1], piles[right])
            gain_last = piles[right] - max(piles[left], piles[right-1])
            if gain_first > gain_last:
                if turns % 2 == 0:
                    score_Alex += piles[left]
                else:
                    score_Lee += piles[left]
                left += 1
            else:
                if turns % 2 == 0:
                    score_Alex += piles[right]
                else:
                    score_Lee += piles[right]
                right -= 1
        return score_Alex > score_Lee