from tuple_to_tree import parse_tuple


def pre_order_traverse(tree_object):
    if tree_object is not None:
        return  [tree_object.data] + pre_order_traverse(tree_object.left) + pre_order_traverse(tree_object.right)
    else:
        return []


tree_tuple = (((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
x = parse_tuple(tree_tuple)
y = pre_order_traverse(x)
print(y)