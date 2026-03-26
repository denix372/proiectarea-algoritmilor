# Note that the problem can be solved using DP
def wordBreak(i, s, dictionary):
    if i == len(s):
        return True
    n = len(s)
    prefix = ""
    for j in range(i, n):
        prefix += s[j]

        if prefix in dictionary and wordBreak(j + 1, s, dictionary):
            return True
    return False

s = "leetcode"
dictionary = {"leet", "code"}
print(wordBreak(0, s, dictionary))