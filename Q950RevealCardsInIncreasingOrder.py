class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        if len(deck) == 1:
            return deck
        deck.sort()
        newOrder = [0]*len(deck)
        locs = [n for n in range(len(deck))]
        i = 0
        while len(locs):
            newOrder[locs.pop(0)] = deck[i]
            i += 1
            if len(locs) == 0:
                break
            n = locs.pop(0)
            locs.append(n)
        return newOrder