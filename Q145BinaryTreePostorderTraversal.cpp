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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ans;
        if(root==nullptr) return ans;
        helper(root, ans);
        return ans;
    }
    
    void helper(TreeNode* root, vector<int>& v)
    {
        if(root == nullptr)
            return;
        helper(root->left, v);
        helper(root->right, v);
        v.push_back(root->val);
        return;
    }
};