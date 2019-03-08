/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int countNodes(TreeNode* root) {
        if(root==nullptr) return 0;
        int heightLeft = heightLeftMost(root->left);
        int heightRight = heightLeftMost(root->right);
        if(heightLeft == heightRight)
            return pow(2, heightLeft) + countNodes(root->right);
        else
            return countNodes(root->left) + pow(2, heightRight);
    }
    int heightLeftMost(TreeNode* root)
    {
        if(root == nullptr) return 0;
        return 1+heightLeftMost(root->left);
    }
};