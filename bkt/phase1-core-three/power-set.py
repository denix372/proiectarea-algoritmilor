def powerSet(string):
    string = "".join(sorted(string))
    n = len(string)

    def back(index, sol):
        if index == n:
            return
        
        if len(sol) > 0:
            print(sol)

        for i in range(index + 1, n):
            sol += string[i]
            back(i, sol)
            sol = sol[: len(sol) - 1]

    back( -1, "")
    return


string = "cab"
powerSet(string)