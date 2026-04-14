class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""

        for s in strs:
            ans += str(len(s)) + "/" + s
        return ans

    def decode(self, s):
        decoded = []
        i = 0
        while i < len(s):
            ind = s.find("/", i)
            length = int(s[i:ind])
            i = ind + 1             
            word = s[i:i+length]
            decoded.append(word)

            i += length

        return decoded 



