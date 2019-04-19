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
    bool isValidBST(TreeNode* root) {
        vector<int> inorder = InorderTraversal(root);
        bool up = true;
        for(int i=1;i<inorder.size();i++)
            if(inorder[i] <= inorder[i-1])
            {
                up = false;
                break;
            }
        return up;
    }
    
    vector<int> InorderTraversal(TreeNode* root)
    {
        vector<int> res;
        if(root==nullptr) return res;
        stack<TreeNode*> sta;
        sta.push(root);
        TreeNode* cur = root->left;
        while(!sta.empty() || cur!=nullptr)
        {
            if(cur == nullptr)
            {
                res.push_back(sta.top()->val);
                cur = sta.top()->right;
                sta.pop();
            }
            else
            {
                sta.push(cur);
                cur = cur->left;
            }
        }
        return res;
    }
};