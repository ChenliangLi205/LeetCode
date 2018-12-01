# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """

        def score(w1, w2):
            s = 0
            for char1, char2 in zip(w1, w2):
                if char1 == char2:
                    s += 1
            return s

        wordPool = wordlist
        for g in range(10):
            length = len(wordPool)
            if length == 0:
                break
            if length == 1:
                master.guess(wordPool[0])
                break
            scoreMatrix = [[6] * length for _ in range(length)]
            for i in range(length):
                for j in range(i + 1, length):
                    scoreMatrix[i][j] = score(wordPool[i], wordPool[j])
            for i in range(length):
                for j in range(i):
                    scoreMatrix[i][j] = scoreMatrix[j][i]
            min_ = length
            nextWord = 0
            for i in range(length):
                counts = [0] * 6
                for j in range(length):
                    if j == i:
                        continue
                    counts[scoreMatrix[i][j]] += 1
                max_ = max(counts)
                if max_ < min_:
                    nextWord = i
                    min_ = max_
            common = master.guess(wordPool[nextWord])
            if common == 6:
                break
            wordPool = [wordPool[j] for j in range(length) if scoreMatrix[nextWord][j] == common]

        return