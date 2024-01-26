`from balanced_tree_check import is_balanced_tree
from bst_with_parent import BSTNode, insert, list_all


def sorted_balanced_tree(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None
    mid = (lo + hi) // 2
    key, value = data[mid]
    node = BSTNode(key=key, value=value)
    node.parent = parent
    node.left = sorted_balanced_tree(data, lo=lo, hi=mid-1, parent=node)
    node.right = sorted_balanced_tree(data, lo=mid+1, hi=hi, parent=node)
    return node


# data = [(3, 's'), (12, 'x'), (12, 'x'), (6, 'a'), (9, 'h'), (13, 'i'), (14, 'l'), (16, 'b'), (19, 'a'), (21, 'r'), (23, 'e'), (33, 'j'),
#         (33, 'a')]

data = [(3, 's'), (12, 'x'), (32, 'x'), (6, 'a'), (9, 'h'), (13, 'i'), (14, 'l'), (16, 'b'), (19, 'a'), (21, 'r'), (23, 'e'), (33, 'j')]
tree = None
for d in data:
    tree = insert(tree, d[0], d[1])
print(is_balanced_tree(tree))
print(list_all(tree))
print(is_balanced_tree(sorted_balanced_tree(list_all(tree))))
# print(is_balanced_tree(list_all(tree)))
# tree = sorted_balanced_tree(data)
# print(is_balanced_tree(tree))