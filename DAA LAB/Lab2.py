# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char  # Character
        self.freq = freq  # Frequency of the character
        self.left = None  # Left child
        self.right = None  # Right child

# Function to sort nodes based on frequency
def sort_nodes(nodes):
    return sorted(nodes, key=lambda x: x.freq)

# Function to generate Huffman codes
def generate_codes(node, current_code, huffman_codes):
    if node is None:
        return

    # If it's a leaf node (character node), add the current code
    if node.char is not None:
        huffman_codes[node.char] = current_code
        return

    # Traverse the left and right subtrees
    generate_codes(node.left, current_code + "0", huffman_codes)
    generate_codes(node.right, current_code + "1", huffman_codes)

# Function to build Huffman Tree and return root
def build_huffman_tree(char_freq):
    # Create initial list of nodes
    nodes = [Node(char, freq) for char, freq in char_freq.items()]

    # Continue until only one node is left (the root of the Huffman Tree)
    while len(nodes) > 1:
        # Sort nodes by frequency in ascending order
        nodes = sort_nodes(nodes)

        # Extract the two nodes with the smallest frequency
        node1 = nodes.pop(0)
        node2 = nodes.pop(0)

        # Create a new internal node with frequency equal to the sum of the two
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        # Insert the new node into the list of nodes
        nodes.append(merged)

    # The root node of the Huffman Tree
    return nodes[0]

# Main function to implement Huffman Encoding
def huffman_encoding(char_freq):
    # Build the Huffman Tree
    root = build_huffman_tree(char_freq)

    # Generate Huffman codes
    huffman_codes = {}
    generate_codes(root, "", huffman_codes)

    return huffman_codes

# User Input
print("Enter the number of characters:")
n = int(input())

char_freq = {}
print("Enter the characters and their frequencies:")
for _ in range(n):
    char = input("Character: ")
    freq = int(input(f"Frequency of '{char}': "))
    char_freq[char] = freq

# Get the Huffman Codes
huffman_codes = huffman_encoding(char_freq)

# Display the Huffman Codes
print("\nHuffman Codes:")
for char, code in huffman_codes.items():
    print(f"'{char}': {code}")
