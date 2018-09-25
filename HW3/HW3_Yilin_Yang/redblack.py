## Yilin Yang
## Data Structures HW 3 - Q1

## Red Black Tree API


class Node:

    path = -1
    leaves = 0
    redblack = 0
    red = 0    

    ## initialization
    def __init__(self, data):
        self.data = [data]
        self.parent = None
        self.child = list()

    ## overload str to print node
    def __str__(self):
        if self.parent: return '   ' + str(self.parent.data) + ' -> ' + str(self.data)
        return str(self.data)

    ## overload less than operator to sort nodes
    def __lt__(self, node):
        return self.data[0] < node.data[0]

    ## check if node is leaf
    def leaf(self):
        return len(self.child) == 0

    ## add new element to tree (helper function for insert)
    def add(self, node):
        for i in node.child:
            i.parent = self
        self.data.extend(node.data)
        self.data.sort()
        self.child.extend(node.child)

        if len(self.child) > 1: self.child.sort()
        if len(self.data) > 2: self.split()
        
    ## locate node in tree to insert
    def insert(self, node):
        if self.leaf(): self.add(node)

        elif node.data[0] > self.data[-1]: self.child[-1].insert(node)

        else:
            for i in  range(0, len(self.data)):
                if node.data[0] < self.data[i]:
                    self.child[i].insert(node)
                    break

    ## split 4 node
    def split(self):
        left = Node(self.data[0])
        right = Node(self.data[2])
        if self.child:
            self.child[0].parent = left
            self.child[1].parent = left
            self.child[2].parent = right
            self.child[3].parent = right
            left.child = [self.child[0], self.child[1]]
            right.child = [self.child[2], self.child[3]]
        self.child = [left]
        self.child.append(right)
        self.data = [self.data[1]]

        if self.parent:
            if self in self.parent.child: self.parent.child.remove(self)
            self.parent.add(self)
        else:
            left.parent = self
            right.parent = self

    ## find element x in tree if it exists
    def find(self, x):
        if x in self.data: return x
        elif self.leaf(): return False
        elif x > self.data[-1]: return self.child[-1].find(x)
        else:
            for i in range(len(self.data)):
                if x < self.data[i]: return self.child[i].find(x)

    ## delete
    def remove(self, x):
        pass

    ## calculate path length
    def count(self, path):
##        print(self)
        Node.redblack += 1
        if (len(self.data) == 2): # 3-nodes count twice
            Node.red += 1
            path += 1
        path += 1
        if self.leaf(): # at a leaf node, add the path to total counter
            Node.path += path 
            Node.leaves += 1
##            print("Path Length: ", Node.path, Node.leaves)            
        for i in self.child:
            i.count(path) # each child will continue counting path length individually

    def reset(self):
        Node.redblack = 0
        Node.red = 0
