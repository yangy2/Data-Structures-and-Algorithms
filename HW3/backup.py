class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val
        self.N = 0

def binary_insert(root, node):
    if root is None:
        root = node
    else:
        root.N += 1
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
                node.N += 1
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
                node.N += 1
            else:
                binary_insert(root.r_child, node)

def size(root):
    if root is None: return 0
    return root.N

# Find rank of given key in root tree
# (the # of nodes key is greater than)
def rank(root, key):
    if root is None: return 0
##    print(size(root), key)
##    print("Root Key: ", root.data)
    if key < root.data: return rank(root.l_child, key)
    elif key > root.data: return 1 + size(root.l_child) + rank(root.r_child, key)
    else: return size(root.l_child)

# Find key of of given rank in root tree
# (only one key has one particular rank) 
def select(root, target_rank):
    if root is None: return 0
    node_rank = rank(r, root.data)
    if target_rank < node_rank: return select(root.l_child, target_rank)
    elif target_rank > node_rank: return select(root.r_child, target_rank)
    else: return root.data

def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print (chr(root.data), root.N)
    in_order_print(root.r_child)

def pre_order_print(root):
    if not root:
        return        
    print (chr(root.data), root.N)
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)  

r = Node(ord("s"))
r.N += 1
binary_insert(r, Node(ord("e")))
binary_insert(r, Node(ord("a")))
binary_insert(r, Node(ord("r")))
binary_insert(r, Node(ord("c")))
binary_insert(r, Node(ord("h")))
binary_insert(r, Node(ord("x")))
binary_insert(r, Node(ord("m")))

print ("in order:")
in_order_print(r)

print ("pre order")
pre_order_print(r)

print ("rank", rank(r, ord("x")))

print ("select", chr(select(r, 3)))
