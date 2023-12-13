from tuple_to_tree import parse_tuple


def is_balanced_tree(node):
    if node is None:
        return True, 0
    balanced_tree_l, height_l = is_balanced_tree(node.left)
    balanced_tree_r, height_r = is_balanced_tree(node.right)
    balanced_tree = balanced_tree_l and balanced_tree_r and abs((height_l - height_r)) <=1
    height = 1 + max(height_l, height_r)
    return balanced_tree, height


# tree2 = parse_tuple(((5, 4, 6), 7, None))
# print(is_balanced_tree(tree2))
