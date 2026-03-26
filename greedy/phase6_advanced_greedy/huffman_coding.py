import heapq

class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(chars, freq):
    heap = []

    for c, f in zip(chars, freq):
        heapq.heappush(heap, Node(f, c))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(left.freq + right.freq, None, left, right)
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(root):
    codes = {}

    def dfs(node, path):
        if node.char is not None:
            codes[node.char] = path or "0"
            return
        dfs(node.left, path + "0")
        dfs(node.right, path + "1")

    dfs(root, "")
    return codes


def huffman_codes(chars, freq):
    root = build_huffman_tree(chars, freq)
    return generate_codes(root)


s = "abcdef"
freq = [5, 9, 12, 13, 16, 45]

codes = huffman_codes(s, freq)
print(codes)