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
    TreeNode* insert(TreeNode* root, TreeNode* newNode){
        if(newNode == NULL) return root;
        if(root == NULL){
            root = newNode;
            return root;
        }
        if(root->val < newNode->val)
            root->right = insert(root->right, newNode);
        else
            root->left = insert(root->left, newNode);
        return root;
    }
    TreeNode* deleteNode(TreeNode* root, int key) {
        if(root == NULL) return root;
        if(root->val == key){
            if(!root->left && !root->right)
                return NULL;
            if(root->left){
                root->val = root->left->val;
                TreeNode* tmp = root->left;
                root->left = tmp->left;
                root->right = insert(root->right, tmp->right);
            }
            else{
                root->val = root->right->val;
                TreeNode* tmp = root->right;
                root->right = tmp->right;
                root->left = tmp->left;
            }
            return root;
        }
        if(root->val < key)
            root->right = deleteNode(root->right, key);
        if(root->val > key)
            root->left = deleteNode(root->left, key);
        return root;
    }
};