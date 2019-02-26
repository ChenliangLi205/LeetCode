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
    int Height(TreeNode* root){
        if(root==nullptr) return 0;
        if(root->left == nullptr && root->right == nullptr) return 1;
        int hLeft = Height(root->left);
        int hRight = Height(root->right);
        return hLeft < hRight? 1+hRight: 1+hLeft;
    }
    
    bool isBalanced(TreeNode* root) {
        if(root==nullptr) return true;
        if(root->left==nullptr && root->right==nullptr) return true;

        int hLeft = Height(root->left);
        int hRight = Height(root->right);
        if(hLeft == hRight || abs(hLeft-hRight) <= 1)
            return isBalanced(root->left) && isBalanced(root->right);
        else return false;
    }
};