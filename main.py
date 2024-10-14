import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None  # Left child
        self.right = None  # Right child

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(input_string):
    """Builds the Huffman tree from the input string and returns the root node."""
    frequency = defaultdict(int)
    for char in input_string:
        frequency[char] += 1

    priority_queue = []
    for char, freq in frequency.items():
        heapq.heappush(priority_queue, Node(char, freq))

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)  # Internal node
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)
    
    return priority_queue[0]

def generate_codes(node, prefix="", codebook={}):
    """Generates the Huffman codes for each character in the tree."""
    if node.char is not None:  # Leaf node
        codebook[node.char] = prefix
    else:  # Internal node
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
    return codebook

def Huffman_coding(input_string):
    """Encodes the input string using Huffman coding."""
    if not input_string:  # Check for empty input
        return ""

    # Step 1: Build Huffman Tree
    huffman_tree_root = build_huffman_tree(input_string)

    # Step 2: Generate Huffman codes
    codebook = generate_codes(huffman_tree_root)

    # Step 3: Encode the input string using the generated codes
    encoded_string = ''.join(codebook[char] for char in input_string)
    
    return encoded_string

# Example usage
if __name__ == "__main__":
    input_string = "this is an example for huffman encoding"
    encoded_string = Huffman_coding(input_string)
    print("Encoded string:", encoded_string)
