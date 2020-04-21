

class Tree(Object):

    def __init__(self, v):
        self.left = None
        self.right = None
        self.val = v

def create( inorder ):
    root = Tree(inorder[0])
    root.left = Tree(inorder[1])
    root.right = Tree(inorder[2])
    
    root.left.left = Tree(inorder[3])
    root.left.right = Tree(inorder[4])

    root.right.left =Tree(inorder[5])
    root.right.right =Tree(inorder[6])


tree = [1,2,3,4,5,6,7,8,9]

expl = []
front = []

def dfs(node):
    expl.append(node)
    front.append(node.left)
    front.append(node(right)
    
    n = front.pop()
    if n not in expl:
        dfs(n)

    
def bfs(node):
    expl.append(node)
    front.append(node.left)
    front.append(node(right)
    
    n = front[0]
    front = front[1:]
    
    if n not in expl:
        bfs(n)

if __name__ == 'main':
    tree = create([1,2,3,4,5,6])
    dfs(tree)
    bfs(tree)

    

