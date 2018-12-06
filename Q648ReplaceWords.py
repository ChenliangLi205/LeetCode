class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        rootSet = set(dict)
        words = sentence.split()
        for i in range(len(words)):
            for j in range(min(len(words[i]), 100)):
                if words[i][:j+1] in rootSet:
                    words[i] = words[i][:j+1]
        return " ".join(words)