class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {' ': ' '}
        letter = 97
        for x in key:
            if x not in d:
                d[x] = chr(letter)
                letter += 1
        
        res = ''
        for x in message:
            res += d[x]
        return res

key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
print(Solution().decodeMessage(key, message))