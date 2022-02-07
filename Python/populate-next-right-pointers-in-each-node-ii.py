#submitted 17/01/2022
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        queue = [root]
        while queue:
            secondary = []
            for i in range(len(queue) - 1):
                queue[i].next = queue[i+1]
                if queue[i].left:
                    secondary.append(queue[i].left)
                if queue[i].right:
                    secondary.append(queue[i].right)
            if queue[-1].left:  
                secondary.append(queue[-1].left)
            if queue[-1].right:
                secondary.append(queue[-1].right)
        
            queue = secondary
        return root