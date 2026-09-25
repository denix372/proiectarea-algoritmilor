from collections import defaultdict

class Solution:
    def find_repeated_dna_sequences(self, s: str) -> list[str]:
        d = defaultdict(int)
        for i in range(len(s) - 9):
            d[s[i : i + 10]] += 1
        
        return [i for i in d if d[i] > 1]

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(Solution().findRepeatedDnaSequences(s))