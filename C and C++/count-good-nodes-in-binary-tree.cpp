//submitted 01/01/2021
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


void nToNode(struct TreeNode *node, int n, int *ptr) {
  if (!node) {
    return;
  }
  if (n <= node->val) { 
    (*ptr)++;
    nToNode(node->left, node->val, ptr);
    nToNode(node->right, node->val, ptr);
  } else {
    nToNode(node->left, n, ptr);
    nToNode(node->right, n, ptr);
  }
}

int goodNodes(struct TreeNode* root) {
  int counter = 0;
  int *ptr = &counter;
  nToNode(root, root->val, ptr);
  return *ptr;
}