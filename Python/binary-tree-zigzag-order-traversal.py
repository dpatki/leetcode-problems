#submitted 13/03/2022
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return []
        queue = [root]
        while queue:
            secondary = []
            result.append([])
            for elem in queue:
                result[-1].append(elem.val)
                if elem.left:
                    secondary.append(elem.left)
                if elem.right:
                    secondary.append(elem.right)
            if len(result)%2 == 0:
                result[-1].reverse()
            queue = secondary
        return result