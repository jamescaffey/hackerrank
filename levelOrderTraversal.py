"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def levelOrder(root):
   #Write code Here
    levelOrdered = [root]
    cur = [root]

    while len(cur)>0:
        below = []
        for x in cur:
            if x.left:
                levelOrdered.append(x.left)
                below.append(x.left)
            if x.right:
                levelOrdered.append(x.right)
                below.append(x.right)

        cur = below

    for node in levelOrdered: print node.data,
