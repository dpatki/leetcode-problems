//submitted 02/26/2021
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
    vector<int> list1;
    vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
        getElemsFromTree(root1, list1);
        getElemsFromTree(root2, list1);
        sort(list1.begin(), list1.end());
        return list1;
        
    }
    void getElemsFromTree(TreeNode *root, vector<int> &list) {
        if (!root) {
            return;
        }
        getElemsFromTree(root->left, list);
        list.push_back(root->val);
        getElemsFromTree(root->right, list);
    }
};