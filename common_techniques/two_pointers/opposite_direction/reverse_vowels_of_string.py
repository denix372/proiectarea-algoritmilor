
class Solution:
    def reverseVowels(self, s: str) -> str:
        ls = list(s)
        vowels = set("aeiouAEIOU")
        i, j = 0, len(s) - 1
        while i < j:
            if ls[i] in vowels  and ls[j] in vowels :
                ls[i], ls[j] = ls[j], ls[i]
                i += 1
                j -= 1
            elif ls[i] not in vowels:
                i += 1
            elif ls[j] not in vowels:
                j -= 1
        return "".join(ls)

s = "IceCreAm"
print(Solution().reverseVowels(s))
