from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def list_to_binary_tree(self, lst):
        if not lst:
            return None

        root = TreeNode(lst[0])
        stack = [root]
        i = 1

        while i < len(lst):
            node = stack.pop(0)

            if lst[i] is not None:
                node.left = TreeNode(lst[i])
                stack.append(node.left)
            i += 1

            if i < len(lst) and lst[i] is not None:
                node.right = TreeNode(lst[i])
                stack.append(node.right)
            i += 1

        return root

    def __repr__(self) -> str:
        return str(self.val)

    def zigzag_order(self, root):
        result = []
        q = deque([root] if root else [])
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level = list(reversed(level)) if len(result) % 2 else level
            result.append(level)
        return result


tree = TreeNode()

# works!
print(
    tree.zigzag_order(
        tree.list_to_binary_tree(
            [1, 2, 3, 4, 5, None, None, 6, 7, 8, 9, None, None, None, None]
        )
    )
)

# does not work!
print(tree.list_to_binary_tree(
            [1, 2, 3, 4, 5, None, 6, 6, 7, None, 1, 6, 7, 8, 9]
        ))
print(
    tree.zigzag_order(
        tree.list_to_binary_tree(
           [1, 2, 3, 4, 5, None, 6, 7, 8, None, 9, 10, 11, 12, 13] 
        )
    )
)
