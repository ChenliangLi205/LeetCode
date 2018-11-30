class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        stack, newInput = "", []
        for char in input:
            if char in "+-*":
                newInput.append(stack)
                stack = ""
                newInput.append(char)
            else:
                stack += char
        newInput.append(stack)

        def calculate(arr):
            if len(arr) == 1:
                return [int(arr[0])]
            results = []
            for i in range(len(arr)):
                char = arr[i]
                if len(char) == 1 and char in "+-*":
                    leftResults, rightResults = calculate(arr[:i]), calculate(arr[i + 1:])
                    for j in leftResults:
                        for k in rightResults:
                            if char == "+":
                                results.append(j + k)
                            elif char == "-":
                                results.append(j - k)
                            else:
                                results.append(j * k)
            return results

        return calculate(newInput)
