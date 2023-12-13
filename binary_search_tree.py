from linear_user_databse import User, UserDatabase
from tuple_to_tree import parse_tuple


def remove_none(datas):
    return [x for x in datas if x is not None]


def is_binary_search_tree(tree_node):
    if tree_node is None:
        return True, None, None

    is_bst_l, min_l, max_l = is_binary_search_tree(tree_node.left)
    is_bst_r, min_r, max_r = is_binary_search_tree(tree_node.right)

    is_bst_node = is_bst_l and is_bst_r and (max_l is None or max_l < tree_node.data) and \
    (min_r is None or min_r > tree_node.data)
    min_key = min(remove_none([min_l, tree_node.data, min_r]))
    max_key = max(remove_none([max_l, tree_node.data, max_r]))

    return is_bst_node, min_key, max_key


tree_tuple = (((1, 3 , None), 4, ((None, 6, 7), 8, (10, 13, 18))))
x = parse_tuple(tree_tuple)
print(is_binary_search_tree(x))
# neeraj = User("neeraj", "neeraj", "neeraj@gmail.com")
# akash = User("akash", "akash", "akash@gmail.com")
# bunty = User("bunty", "bunty", "bunty@gmail.com")
# chunnu = User("chunnu", "chunnu", "chunnu@gmail.com")
# dheeraj = User("dheeraj", "dheeraj", "dheeraj@gmail.com")
# deepak = User("deepak", "deepak", "deepak@gmail.com")
# user_database = UserDatabase()
# user_database.insert(neeraj)
# user_database.list_all()
# user_database.insert(akash)
# user_database.list_all()
# user_database.insert(bunty)
# user_database.list_all()
# user_database.insert(chunnu)
# user_database.list_all()
# user_database.insert(dheeraj)
# user_database.list_all()
# user_database.insert(deepak)
# user_database.list_all()
# print(is_bst(user_database))

tree2 = parse_tuple((('aakash', 'biraj', 'hemanth'), 'jadhesh', ('siddhant', 'sonaksh', 'vishal')))
print(is_binary_search_tree(tree2))
