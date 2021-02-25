//submitted 02/19/2021
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
    vector<int> values;
    bool isValidBST(TreeNode* root) {
        findValues(root);
        for(int i =0; i < values.size() - 1; i++) {
            cout << values[i] << values[i+1] <<" ";
            if (values[i] >= values[i+1]) {
                return false;
            }
        }
        return true;
    }
    
    void findValues(TreeNode *node) {
        if (!node) {
            return;
        }
        if (node->left) {
            findValues(node->left);
        }
        values.push_back(node->val);
        if (node->right) {
            findValues(node->right);
        }
    }
};