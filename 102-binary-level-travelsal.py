# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        final_tree = []
        if len(root) == 0:
            return root
        if len(root) == 1:
            return [root]
        tree_nodes = [pow(2, 0), pow(2, 1), pow(2, 2), pow(2, 3), pow(2, 4), pow(2, 5), pow(2, 6), pow(2, 7)]
        k = 0
        for i in tree_nodes:
            x = []
            new_i = i+k
            while k < new_i:
                try:
                    if root[k] is not None:
                        x.append(root[k])
                    k += 1
                except IndexError as ex:
                    final_tree.append(x)
                    return final_tree
            final_tree.append(x)
        return final_tree

print(Solution().levelOrder([3,9,20,None,None,15,7, 3]))