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
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> ans;
        if(root==nullptr) return ans;
        queue<pair<string, TreeNode*>> q;
        q.push(pair<string, TreeNode*>("", root));
        while(!q.empty()){
            pair<string, TreeNode*> curr = q.front();
            q.pop();
            string newStr;
            if(curr.first.empty()) newStr = to_string(curr.second->val);
            else newStr = curr.first + "->" + to_string(curr.second->val);
            if(curr.second->left==nullptr && curr.second->right==nullptr) ans.push_back(newStr);
            else{
                if(curr.second->left!=nullptr) q.push(pair<string, TreeNode*>(newStr, curr.second->left));
                if(curr.second->right!=nullptr) q.push(pair<string, TreeNode*>(newStr, curr.second->right));
            }
        }
        return ans;
    }
};