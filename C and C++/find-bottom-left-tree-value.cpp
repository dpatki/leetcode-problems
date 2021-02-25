//submitted 02/21/2021
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
  int best = 0;
  int deep = -1;

  void recursiveBit(TreeNode *node, int depth) {
    if (!node) {
      return;
    }
    recursiveBit(node->right, depth+1);
    if (depth >= deep) {
      best = node->val;
      deep = depth;
    }
    recursiveBit(node->left, depth+1);
  }


  int findBottomLeftValue(TreeNode* root) {
    recursiveBit(root, 0);
    return best;
  }
  
};