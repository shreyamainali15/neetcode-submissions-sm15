class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "/" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0

        while i < len(s):
            index = s.find("/", i)
            length = int(s[i:index])
            i = index + 1

            word = s[i:i+length]

            decoded.append(word)

            i += length

        return decoded 
            
