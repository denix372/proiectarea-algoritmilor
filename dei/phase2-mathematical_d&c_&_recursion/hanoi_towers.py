
def hanoi(n, fro, to, aux):
    if n == 0:
        return
    
    hanoi(n - 1, fro, aux, to)
    print("Disk", n, " moved from ", fro, " to ", to)
    hanoi(n - 1, aux, to, fro)

n = 3
hanoi(n, 'A', 'C', 'B')