class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            encoded += str(len(word)) + "#" + word

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0 

        while i < len(s):
            char = s.find("#", i)
            length = int(s[i:char])

            i = char + 1

            word = s[i:i+length]

            decoded.append(word)

            i += length

        return decoded
