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
    int sumNumbers(TreeNode* root) {
        if(root == nullptr) return 0;
        if(root->left==nullptr && root->right==nullptr) return root->val;
        int ans = 0;
        int starting=root->val;
        queue<pair<int, TreeNode*>> q;
        if(root->left != nullptr)
            q.push(make_pair(starting, root->left));
        if(root->right != nullptr)
            q.push(make_pair(starting, root->right));
        while(!q.empty())
        {
            pair<int, TreeNode*> thisPair = q.front();
            if(thisPair.second->left == nullptr && thisPair.second->right == nullptr)
                ans += thisPair.first*10 + thisPair.second->val;
            else
            {
                int newNum = thisPair.first*10 + thisPair.second->val;
                if(thisPair.second->left!=nullptr)
                    q.push(make_pair(newNum, thisPair.second->left));
                if(thisPair.second->right != nullptr)
                    q.push(make_pair(newNum, thisPair.second->right));
            }
            q.pop();
        }
        return ans;
    }
};