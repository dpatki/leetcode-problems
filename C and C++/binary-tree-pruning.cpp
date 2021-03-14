//submitted 03/07/21

class Solution {
public:
    TreeNode* pruneTree(TreeNode* root) {
        if(!hastruechild(root)) {
            return nullptr;
        }
        delchildnodes(root);
        return root;
        
    }
    bool hastruechild(TreeNode* node) {
        if (!node) {
            return false;
        }
        if (node->val == 1) {
            return true;
        }
        return (hastruechild(node->left) || hastruechild(node->right));
        
    }
    void delchildnodes(TreeNode * node) {
        if (!node) {
            return;
        }
        if (!hastruechild(node->left)) {
            node->left = nullptr;
        }
        if(!hastruechild(node->right)) {
            node->right = nullptr;
        }
        delchildnodes(node->right);
        delchildnodes(node->left);
        
    }
};