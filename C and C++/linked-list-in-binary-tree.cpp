//submitted 02/05/2021
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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
  
  bool recursiveBit(TreeNode* node, ListNode *thingy) {
    if (!node) {
      return false;
    }
    if (thingy->val == node->val){
      if (!thingy->next) {
        return true;
      } else {
        return (recursiveBit(node->left, thingy->next) || recursiveBit(node->right, thingy->next) );
      }
    }
    return false;
  }

  bool isSubPath(ListNode* head, TreeNode* root) {
    if (!root) {
      return false;
    }
    return recursiveBit(root, head) || isSubPath(head,root->left) || isSubPath(head, root->right);

  }
};