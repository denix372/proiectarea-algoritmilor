def optimalKeys(n):
    if n <= 6:
        return n

    screen = [0] * n
    for i in range(1, 7):
        screen[i - 1] = i

    for i in range(7, n + 1):
        
        screen[i - 1] = max(2 * screen[i - 4],
                            max(3 * screen[i - 5],
                                4 * screen[i - 6]))

    return screen[n - 1]


if __name__ == "__main__":
    n = 7
    print(optimalKeys(n))