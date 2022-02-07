#submitted 17/01/2022
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        queue = [root]
        while queue:
            secondary = []
            for i in range(len(queue) - 1):
                queue[i].next = queue[i+1]
                secondary.append(queue[i].left)
                secondary.append(queue[i].right)
            secondary.append(queue[-1].left)
            secondary.append(queue[-1].right)
            if secondary[0] == None:
                break
            queue = secondary
        return root
            