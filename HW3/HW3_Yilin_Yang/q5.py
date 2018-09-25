#Yilin Yang
#Data Structures & Algorithms HW3

# Define node in BST
# has 2 children, a key, and a node count
class Node:
    def __init__(self, key):
        self.l_child = None
        self.r_child = None
        self.data = key
        self.N = 0

# Insert node into tree
def insert(root, node):
    # if tree is empty
    if root is None: root = node

    # if tree is not empty
    else:
        root.N += 1
        # if current node is greater than insertion
        # put insertion in left child
        if root.data > node.data:
            # if there is no left child
            if root.l_child is None:
                root.l_child = node
                node.N += 1
            # if there is a left child
            else: insert(root.l_child, node)

        # if current node is less than insertion
        # put insertion in right child
        else:
            # if there is no right child
            if root.r_child is None:
                root.r_child = node
                node.N += 1
            # if there is a right child
            else: insert(root.r_child, node)

# Return node count of given node
def size(root):
    if root is None: return 0
    return root.N

# Find rank of given key in root tree
# (the # of nodes the key is greater than)
def rank(root, key):
    if root is None: return 0

    # if key is less than current node, search left subtree
    if key < root.data: return rank(root.l_child, key)
    
    # if key is greater than current node, search right subtree
    # include all nodes to left including current node when counting rank
    elif key > root.data: return 1 + size(root.l_child) + rank(root.r_child, key)
    
    # if key matches current node, return size of left subtree
    else: return size(root.l_child)

# Find key of of given rank in root tree
# (each key has only one rank) 
def select(root, target_rank):
    if root is None: return 0
    node_rank = rank(tree, root.data)

    # if rank is less than current node rank, search left subtree
    if target_rank < node_rank: return select(root.l_child, target_rank)

    # if rank is greater than current node rank, search right subtree
    elif target_rank > node_rank: return select(root.r_child, target_rank)

    # if rank matches current node rank, return current node key
    else: return root.data

# Print elements in ascending order
def printtree(root):
    if not root: return
    printtree(root.l_child)
    print (root.data, root.N)
    printtree(root.r_child)

# Read from external file and put into list
def readfile(numList, filepath):
    with open(filepath) as f:
        line = f.readline()
        while line:
            numList.append(int(line.strip('\n')))
            line = f.readline()
            
file = "data.txt"
numList = [] #create list
readfile(numList, file) #fill list with data
x = len(numList) #length of list

# initialize BST
tree = Node(numList[0])
tree.N += 1

# fill BST
print("Filling Tree")

numList2 = []
for i in range(0,x):
    if numList[i] not in numList2: # remove duplicate keys
        numList2.append(numList[i])
y = len(numList2)

for i in range(1,y): insert(tree, Node(numList2[i]))
print("Tree Filled")

# print BST
##printtree(tree)

rank_search = 7
select_search = 7

print ("Rank of", str(rank_search) + ":", rank(tree, rank_search))
print ("Select of", str(select_search) + ":", select(tree, select_search))

