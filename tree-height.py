from tuple_to_tree import parse_tuple


def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))


tree_tuple = (((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
x = parse_tuple(tree_tuple)
y = tree_height(x)
print(y)