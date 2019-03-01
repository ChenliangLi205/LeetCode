/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class BSTIterator {
public:
    TreeNode* currNode;
    vector<TreeNode*> ancestors;
    vector<int> isLeft;
    
    BSTIterator(TreeNode* root) {
        locateSmallest(root);
    }
    
    void locateSmallest(TreeNode* root)
    {
        if(root == nullptr) 
        {
            currNode = nullptr;
            return;
        }
        currNode = root;
        while(currNode->left!=nullptr)
        {
            isLeft.push_back(1);
            ancestors.push_back(currNode);
            currNode = currNode->left;
        }
    }
    
    /** @return the next smallest number */
    int next() {
        if(currNode == nullptr) return 0;
        int res = currNode->val;
        nextSmallest();
        return res;
    }
    
    void nextSmallest()
    {
        if(currNode == nullptr) return;
        if(currNode->right != nullptr)
        {
            isLeft.push_back(0);
            ancestors.push_back(currNode);
            locateSmallest(currNode->right);
            return;
        }
        if(isLeft.size()==0)
        {
            currNode = nullptr;
            return;
        }
        while(isLeft.size()>0 && isLeft.back()==0)
        {
            isLeft.pop_back();
            ancestors.pop_back();
        }
        if(isLeft.size()==0)
            currNode = nullptr;
        else
        {
            currNode = ancestors.back();
            ancestors.pop_back();
            isLeft.pop_back();
        }
    }
    
    /** @return whether we have a next smallest number */
    bool hasNext() {
        return currNode != nullptr;
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */