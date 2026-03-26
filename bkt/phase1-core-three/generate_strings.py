"""
You are given a list of distinct characters and a corresponding list of frequencies,
where freq[i] represents how many times character chars[i] must appear in the final strings.

Your task is to generate all possible strings that can be formed using exactly these
frequencies, under the following constraint:

    No character may appear more than K times consecutively.

All valid strings must be generated in strict lexicographical order.

Input:
    chars[] - array of distinct characters, already sorted lexicographically
    freq[]  - array of positive integers, same length as chars[]
    K       - maximum allowed number of consecutive occurrences of the same character

Output:
    A list of all lexicographically ordered strings that satisfy the frequency
    requirements and the consecutive-occurrence constraint.

"""
def solve(chars, freq, k):
    n = len(chars)
    res = []

    def bkt(sol, freq, last_char, last_count):
        if sum(freq) == 0:
            res.append(sol)
            return

        for i in range(n):
            if freq[i] != 0:
                if chars[i] == last_char and last_count == k:
                    continue

                freq[i] -= 1

                if last_char == chars[i]:
                    bkt(sol + chars[i], freq.copy(), chars[i], last_count + 1)
                else:
                    bkt(sol + chars[i], freq.copy(), chars[i], 1)
                freq[i] += 1

    bkt("", freq, None, 0)
    return res

chars = ['b', 'c']
freq = [3, 2]
k = 2
for x in solve(chars, freq, k):
    print(x)