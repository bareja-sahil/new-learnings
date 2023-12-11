from tuple_to_tree import parse_tuple


def post_order_traverse(tree_object):
    if tree_object is not None:
        return post_order_traverse(tree_object.left) + post_order_traverse(tree_object.right) + [tree_object.data]
    else:
        return []


tree_tuple = (((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
x = parse_tuple(tree_tuple)
y = post_order_traverse(x)
print(y)