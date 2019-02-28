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
    void flatten(TreeNode* root) {
        helper(root);
    }
    
    TreeNode* helper(TreeNode* root)
    {
        if(root == nullptr) return nullptr;
        if(root->left == nullptr && root->right == nullptr)
            return root;
        if(root->left == nullptr)
            return helper(root->right);
        if(root->right == nullptr)
        {
            root->right = root->left;
            root->left = nullptr;
            return helper(root->right);
        }
        TreeNode* tmp = root->right;
        root->right = root->left;
        root->left = nullptr;
        TreeNode* tail = helper(root->right);
        tail->left = nullptr;
        tail->right = tmp;
        return helper(tail->right);
    }
};