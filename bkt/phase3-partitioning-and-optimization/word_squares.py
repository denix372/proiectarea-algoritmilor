from collections import defaultdict

def solve(words):
    n = len(words)

    #  Build a Prefix Dictionary
    # Example: for "ball", we store:
    # "" -> "ball", "b" -> "ball", "ba" -> "ball", "bal" -> "ball", "ball" -> "ball"
    prefix_map = defaultdict(list)
    for word in words:
        for i in range(n + 1):
            prefix_map[word[:i]].append(word)
    res =[]

    def back(i, sol):
        if i == n:
            res.append(sol.copy())
            return

        # # We take the 'step'-th character of every word currently in our square
        prefix = "".join(word[i] for word in sol)

        # # Only iterate through words that perfectly match the required prefix
        for c in prefix_map[prefix]:
            sol.append(c)
            back(i + 1, sol)
            sol.pop()

    # first word can be any word in the list
    for word in words:
        back(1, [word])
    return res

words = ["abat","baba","atan","atal"]
for r in solve(words):
    print(*r)