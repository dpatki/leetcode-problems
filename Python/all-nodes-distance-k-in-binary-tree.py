#submitted 11/04/2021
class Solution:
    nodes = collections.defaultdict(list)

    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        self.nodes = defaultdict(list)
        self.traverse(root, None)
        print(self.nodes)
        seen = [target.val]
        stick = self.nodes[target.val]
        print(stick, " stick")
        if K == 0:
            return [target.val]
        i = 1
        while (i < K):
            stonk = []
            for elem in stick:
                seen.append(elem)
                things = self.nodes[elem]
                for thingy in things:
                    if thingy not in seen:
                        stonk.append(thingy)
            print(stonk, " stonk")
            stick = stonk
            i += 1
  
        return stick

    def traverse(self, node, parent):
        if parent != None:
            self.nodes[node.val].append(parent.val)
        if (node.left) != None:
            self.nodes[node.val].append(node.left.val)  
        if (node.right) != None:
            self.nodes[node.val].append(node.right.val)
        if node.left != None:
            self.traverse(node.left, node)
        if node.right != None:
            self.traverse(node.right, node)