from linear_user_databse import User


class BSTNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


def insert(tree, key, value):
    if tree is None:
        node = BSTNode(key, value)
        return node
    if key < tree.key:
        tree.left = insert(tree.left, key, value)
        tree.left.parent = tree
        return tree
    if key > tree.key:
        tree.right = insert(tree.right, key, value)
        tree.right.parent = tree
        # node.parent = tree
        return tree


def find(tree, key, value):
    if tree is None:
        return None
    if tree.key == key:
        return tree
    if key < tree.key:
        node = find(tree.left, key, value)
        return node
    if key > tree.key:
        return find(tree.right, key, value)


def update(node, key, value):
    target = find(node, key, value)
    if target is not None:
        target.value = value


def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)

#
# tree = None
# neeraj = User("neeraj", "neeraj", "neeraj@gmail.com")
# tree = insert(tree, neeraj.username, neeraj)
# akash = User("akash", "akash", "akash@gmail.com")
# tree = insert(tree, akash.username, akash)
# bunty = User("bunty", "bunty", "bunty@gmail.com")
# tree = insert(tree, bunty.username, bunty)
# chunnu = User("chunnu", "chunnu", "chunnu@gmail.com")
# tree = insert(tree, chunnu.username, chunnu)
# dheeraj = User("dheeraj", "dheeraj", "dheeraj@gmail.com")
# tree = insert(tree, dheeraj.username, dheeraj)
# deepak = User("deepak", "deepak", "deepak@gmail.com")
# tree = insert(tree, deepak.username, deepak)
# print(tree)
#
# print(list_all(tree))
