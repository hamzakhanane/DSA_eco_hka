# Runtime O(n)
# Memory O(n)

def levelOrder(root):
    if root is None: return []
    fill = []
    levelHelper(root, 0, fill)
    return fill

def levelHelper(node, level, fill):
    if len(fill) == level:
        fill.append([])
    fill[level].append(node.val)
    if node.left: levelHelper(node.left, level + 1, fill)
    if node.right: levelHelper(node.right, level + 1, fill)
