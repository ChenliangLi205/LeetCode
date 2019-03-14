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
        map<TreeNode*, TreeNode*> parentDict;
        stack<TreeNode*> toVisit;
        parentDict[root] = nullptr;
        toVisit.push(root);
        TreeNode* curr;
        while(parentDict.find(p)==parentDict.end() || parentDict.find(q)==parentDict.end())
        {
            curr = toVisit.top();
            toVisit.pop();
            if(curr==nullptr) continue;
            if(curr->left!=nullptr){
                if(curr->left == q)
                    cout<<curr->val<<endl;
                parentDict[curr->left] = curr;
                toVisit.push(curr->left);
            }
            if(curr->right!=nullptr){
                parentDict[curr->right] = curr;
                toVisit.push(curr->right);
            }
        }
        set<TreeNode*> ancestors;
        curr = p;
        while(curr!=nullptr){
            ancestors.insert(curr);
            curr = parentDict[curr];
        }
        curr = q;
        while(curr!=nullptr){
            if(ancestors.find(curr)!=ancestors.end())
                return curr;
            ancestors.insert(curr);
            curr = parentDict[curr];
        }
        // for(auto node: ancestors)
        //     cout<<node->val<<" ";
        return root;
    }
};