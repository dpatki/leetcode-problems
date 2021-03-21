//submitted 03/14/2021

class Solution {
public:
    TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {
    TreeNode* parent = traverse(root1, root2);
    return parent;
  }
  TreeNode* traverse(TreeNode* node1, TreeNode *node2) {
    if (node1 == nullptr && node2==nullptr) {
      return nullptr;
    } else if (node1 == nullptr && node2 != nullptr) {
      return node2;
    } else if (node1 != nullptr && node2 == nullptr) {
      return node1;
    }
    TreeNode *right = traverse(node1->right, node2->right);
    TreeNode *left = traverse(node1->left, node2->left);
    node1->val += node2->val;
    node1->right = right;
    node1->left = left;
    return node1;
  }
};