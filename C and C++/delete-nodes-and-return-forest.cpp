//submitted 01/06/2021
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
private:
  vector<TreeNode*> potato;
public:
  vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {

    unordered_set<int> s(to_delete.begin(), to_delete.end());

    if (s.find(root->val) != s.end()) {

    } else {
      potato.push_back(root);
    }
    trackNodes(root, s);
    /*call helper*/
    return potato;

  }

  bool trackNodes(TreeNode* node, unordered_set<int>& s) {
    bool righty = true;
    bool lefty = true;
    if (node->right) {
      righty = trackNodes(node->right, s);
    }
    if (node->left) {
      lefty = trackNodes(node->left, s);
    }

    if (s.find(node->val) != s.end()) {
      if (!righty) {
        potato.push_back(node->right);
      } else {
        node->right = nullptr;
      }
      if (!lefty) {
        potato.push_back(node->left);
      } else {
        node->left = nullptr;
      }

      return true;
    } else {
      if (righty) {
          node->right = nullptr;
      }
      if (lefty) {
         node->left = nullptr;
      }
      return false;
        
  }
  }
};