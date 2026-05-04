class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        res = []
        q = collections.deque([root])

        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level)

        return res