from tuple_to_tree import parse_tuple


def tree_nodes(node):
    if node is None:
        return 0
    return 1 + tree_nodes(node.left) + tree_nodes(node.right)


tree_tuple = (((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, None))))
x = parse_tuple(tree_tuple)
y = tree_nodes(x)
print(y)