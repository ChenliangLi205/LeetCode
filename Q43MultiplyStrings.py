class Solution:
    def strMultiply(self, s, char):
        bonus = 0
        n = int(char)
        newStr = ''
        for i in range(len(s) - 1, -1, -1):
            m = int(s[i])
            result = n * m + bonus
            newChar, bonus = str(result % 10), result // 10
            newStr = newChar + newStr
        if bonus == 0:
            return newStr
        else:
            return str(bonus) + newStr

    def strAdd(self, s1, s2, offset):
        bonus, loc2 = 0, len(s2) - 1
        newStr = s1[len(s1) - offset:]
        for i in range(len(s1) - 1 - offset, -1, -1):
            result = int(s1[i]) + int(s2[loc2]) + bonus
            newChar, bonus = str(result % 10), result // 10
            loc2 -= 1
            newStr = newChar + newStr
        for i in range(loc2, -1, -1):
            result = int(s2[i]) + bonus
            newChar, bonus = str(result % 10), result // 10
            newStr = newChar + newStr
        if bonus == 0:
            return newStr
        else:
            return str(bonus) + newStr

    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        multiplySet = dict()
        result = self.strMultiply(num1, num2[-1])
        multiplySet[num2[-1]] = result
        offset = 1
        for i in range(len(num2) - 2, -1, -1):
            if num2[i] in multiplySet:
                subResult = multiplySet[num2[i]]
            else:
                subResult = self.strMultiply(num1, num2[i])
                multiplySet[num2[i]] = subResult
            result = self.strAdd(result, subResult, offset)
            offset += 1
        return result
