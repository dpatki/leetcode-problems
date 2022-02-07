#submitted 15/01/2022
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        final = []
        queue = [root]
        while len(queue) > 0:
            values = []
            secondary = []
            for elem in queue:
                values.append(elem.val)
                if elem.left:
                    secondary.append(elem.left)
                if elem.right:
                    secondary.append(elem.right)
            queue = secondary
            final.append(values)
        final.reverse()
        return final