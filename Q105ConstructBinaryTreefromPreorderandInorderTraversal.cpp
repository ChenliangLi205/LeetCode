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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if(preorder.size()==0||inorder.size() == 0) return nullptr;
        return helper(preorder, inorder, 0, preorder.size(), 0, inorder.size());
    }
    
    TreeNode* helper(vector<int>& preorder, vector<int>& inorder, int preBeg, int preEnd, int inBeg, int inEnd)
    {
        if(preBeg>=preorder.size()||inBeg>=inorder.size())
            return nullptr;
        if(preBeg-preEnd>=0||inBeg-inEnd>=0)
            return nullptr;
        if(preBeg-preEnd==1||inBeg-inEnd==1)
            return new TreeNode(preorder[preBeg]);
        int i=0;
        for(;i+inBeg<inEnd;i++)
        {
            if(inorder[i+inBeg] == preorder[preBeg])
                break;
        }
        TreeNode* root = new TreeNode(preorder[preBeg]);
        root->left = helper(preorder, inorder, preBeg+1, preBeg+i+1, inBeg, inBeg+i);
        root->right = helper(preorder, inorder, preBeg+i+1, preEnd, inBeg+i+1, inEnd);
        return root;
    }
};