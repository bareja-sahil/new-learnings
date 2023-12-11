class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
        return node
    elif data is None:
        return data
    else:
        return TreeNode(data)


def tree_to_tuple(tree_object):
    if isinstance(tree_object, TreeNode) and (tree_object.left is None and tree_object.right is None):
        return tree_object.data
    elif isinstance(tree_object, TreeNode):
        return tree_to_tuple(tree_object.left), tree_object.data, tree_to_tuple(tree_object.right)
    elif tree_object is not None:
        return tree_object


#
# tree_tuple = (((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
# x = parse_tuple(tree_tuple)
# print(x)
# y = tree_to_tuple(x)
# print(y)
# print(tree_tuple == y)