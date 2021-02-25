//Submitted 12/26/2020


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int sum = 0;
int helper(struct TreeNode *root, int low, int high) {
    if (root->left) {
        helper(root->left, low, high);
    }
    if ((low <= root->val) && (root->val <= high)) {
        printf("sum: %d", sum);
        printf("%d \n", root->val);
        sum += root->val;
    }
    if (root->right) {
        helper(root->right, low, high);
    } 
    
    return sum;
}
int rangeSumBST(struct TreeNode* root, int low, int high){
    if(!root) {
        return 0;
    }
    sum = 0;
    return helper(root, low, high);
}