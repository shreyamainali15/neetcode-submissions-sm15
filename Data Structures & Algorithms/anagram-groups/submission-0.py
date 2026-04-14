class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for words in strs:
            count = [0] * 26

            for char in words:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)

            if key not in ans:
                ans[key] = []

            ans[key].append(words)

        return list(ans.values())
        