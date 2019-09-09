// Runtime O(n)
// Memory O(n)

var levelOrder = function(root) {
    if (!root) return []
    const fill = [];
    const helper = (node, level) => {
        if (fill.length === level) {
            fill.push([]);
        }
        fill[level].push(node.val);
        if (node.left) helper(node.left, level + 1);
        if (node.right) helper(node.right, level + 1);
    }
    helper(root, 0)
    return fill;
};