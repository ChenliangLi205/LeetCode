class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        length = len(hand)
        if length % W != 0:
            return False
        n2cnt = dict()
        for n in hand:
            if n not in n2cnt:
                n2cnt[n] = 0
            n2cnt[n] += 1
        cardSet = set(hand)
        while len(cardSet):
            start = min(cardSet)
            for i in range(start, start+W):
                if i not in n2cnt:
                    return False
                n2cnt[i] -= 1
                if n2cnt[i] == 0:
                    cardSet.remove(i)
        return True