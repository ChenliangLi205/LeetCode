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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root == nullptr) return nullptr;
        TreeNode* curr = root;
        while(curr!=nullptr)
        {
            if(p->val == curr->val || q->val == curr->val)
                return curr;
            if(p->val > curr->val && q->val > curr->val)
            {curr = curr->right;continue;}
            if(p->val < curr->val && q->val < curr->val)
            {curr = curr->left;continue;}
            return curr;
        }
        return curr;
    }
};