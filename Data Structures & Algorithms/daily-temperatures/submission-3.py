class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for temp in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[temp]:
                index = stack.pop()
                result[index] = temp - index
            stack.append(temp)

        return result