import sys

MOD = 10**9 + 7
MAXN = 10**6 + 1

# 1. PRECOMPUTE GLOBALLY (Run this ONCE)
split = [0] * MAXN
joined = [0] * MAXN
res = [0] * MAXN

split[1] = 1
joined[1] = 1
res[1] = 2

for i in range(2, MAXN):
    split[i] = (4 * split[i - 1] + joined[i - 1]) % MOD
    joined[i] = (split[i - 1] + 2 * joined[i - 1]) % MOD
    res[i] = (split[i] + joined[i]) % MOD

if __name__ == '__main__':
    # 2. READ ALL INPUTS
    input_data = sys.stdin.read().split()
    if not input_data:
        sys.exit()
        
    m = int(input_data[0])
    queries = input_data[1:]
    
    output = []
    
    # 3. ANSWER QUERIES IN O(1) TIME
    for q in queries:
        n = int(q)
        # Just grab the answer from our precomputed array!
        output.append(str(res[n]))

    sys.stdout.write('\n'.join(output) + '\n')