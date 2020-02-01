with open('18.txt') as f:
    lines = [line.rstrip() for line in f]
triangle = []
for x in lines:
    temp = x.split(' ')
    temp2 = []
    for y in temp:
        temp2.append(int(y))
    triangle.append(temp2)

def get_best_path_value(n):
    if(not n.has_children()):
        return n.value
    left = get_best_path_value(n.child1)
    right = get_best_path_value(n.child2)
    if(left > right):
        return n.value + left
    else:
        return n.value + right

def generate_list(n, max_depth, pyramid):
    if(n.row == max_depth):
        return
    else:
        n.make_children(linkedNode(pyramid[n.row+1][n.col], n.row+1, n.col), linkedNode(pyramid[n.row+1][n.col+1], n.row+1, n.col+1))
        generate_list(n.child1, max_depth, pyramid)
        generate_list(n.child2, max_depth, pyramid)
        return

class linkedNode:
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.child1 = None
        self.child2 = None

    def has_children(self):
        if(self.child1):
            return True
        else:
            return False

    def make_children(self, child1, child2):
        self.child1 = child1
        self.child2 = child2

class linkedList:
    def __init__(self, pyramid):
        self.root = linkedNode(pyramid[0][0], 0, 0)
        max_depth = len(pyramid) - 1
        generate_list(self.root, max_depth, pyramid)

p = linkedList(triangle)
print(get_best_path_value(p.root))