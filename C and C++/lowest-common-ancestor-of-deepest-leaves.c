//submitted 01/01/2021
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* lca = NULL;
int findDeepestNode(struct TreeNode *root, int depth, int *maxDepth) { 
    if (root->left && root->right) {
        //lca = root;
        int left = findDeepestNode(root->left, depth + 1, maxDepth);
        int right = findDeepestNode(root->right, depth + 1, maxDepth);
        //printf("max: %d", *maxDepth);
        if (*maxDepth == left && *maxDepth == right) {
            lca = root;
        }
        return fmax(left, right);
    
    } else if (root->right) {
        return findDeepestNode(root->right, depth + 1, maxDepth);
    } else if (root->left) {
        return findDeepestNode(root->left, depth + 1, maxDepth);
    }
  
    if(!root->left && !root->right) {
        if (depth + 1 > *maxDepth) {
            *maxDepth = depth;
            lca = root;
        }
        return depth;
    } else {
        printf("horridly wrong\n");
        return depth + 1;
    }
}

struct TreeNode* lcaDeepestLeaves(struct TreeNode* root){
    lca = NULL;
    int maxDepth = 0;
    int *random_ptr = &maxDepth;
   
    int potato = findDeepestNode(root, 0, random_ptr);
    return lca;
}

