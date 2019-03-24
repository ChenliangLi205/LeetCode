/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class SolutionCount {
public:
    int kthSmallest(TreeNode* root, int k) {
        int leftNum = CountTreeNodeNum(root->left);
        if(leftNum>=k) return kthSmallest(root->left, k);
        if(leftNum==k-1) return root->val;
        return kthSmallest(root->right, k-leftNum-1);
    }
    int CountTreeNodeNum(TreeNode* root){
        if(root==nullptr) return 0;
        return 1+CountTreeNodeNum(root->left)+CountTreeNodeNum(root->right);
    }
};

class SolutionInorder {
public:
    int kthSmallest(TreeNode* root, int k) {
        vector<int> visited; 
        InorderTraversal(root, visited, k);
        return visited.back();
    }
    void InorderTraversal(TreeNode* root, vector<int>& v, int k)
    {
        if(v.size() >= k) return;
        if(root->left!=nullptr)
            InorderTraversal(root->left, v, k);
        if(v.size() >= k) return;
        v.push_back(root->val);
        if(v.size() >= k) return;
        if(root->right!=nullptr)
            InorderTraversal(root->right, v, k);
    }
};