//submitted 01/29/2021
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
  unordered_set<int> nummers;
  bool findTarget(TreeNode* root, int k) {
    return traverse(root, k);
  }

  bool traverse(TreeNode *node, int k) {
   if (!node) {
     return false;
   }
   
   int target = k - node->val; 
   if (nummers.find(target) != nummers.end()) {
     return true;
   }
nummers.insert(node->val);
   return (traverse(node->right,k) || traverse(node->left, k));
  }
};