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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ans;
        if(root==nullptr) return ans;
        stack<TreeNode*> s;
        s.push(root);
        while(!s.empty())
        {
            if(s.top()==nullptr)
            {
                s.pop();
                continue;
            }
            ans.push_back(s.top()->val);
            TreeNode* tmp = s.top();
            s.pop();
            s.push(tmp->right);
            s.push(tmp->left);
        }
        return ans;
    }
};