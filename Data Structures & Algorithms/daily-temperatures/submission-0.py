class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ans = [0] * len(temperatures)
        stack = []

        for temp in range(len(temperatures)):
            while stack and temperatures[temp] > temperatures[stack[-1]]:
                index = stack.pop()
                ans[index] = temp - index
            stack.append(temp)
        return ans
        