/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
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
    TreeNode* sortedListToBST(ListNode* head) {
        if(head == nullptr) return nullptr;
        if(head->next == nullptr) return new TreeNode(head->val);
        if(head->next->next==nullptr)
        {
            TreeNode* treeHead = new TreeNode(head->val);
            treeHead->right = new TreeNode(head->next->val);
            return treeHead;
        }
        vector<ListNode*> array;
        ListNode* curr = head;
        while(curr!=nullptr)
        {
            array.push_back(curr);
            curr = curr->next;
        }
        return sortedArrayToBST(array);
    }
    
    TreeNode* sortedArrayToBST(vector<ListNode*> array)
    {
        if(array.size() == 0) return nullptr;
        if(array.size() == 1) return new TreeNode(array[0]->val);
        if(array.size() == 2)
        {
            TreeNode* treeHead = new TreeNode(array[0]->val);
            treeHead->right = new TreeNode(array[1]->val);
            return treeHead;
        }
        int mid = array.size() /2;
        TreeNode* treeHead = new TreeNode(array[mid]->val);
        treeHead->left = sortedArrayToBST(vector<ListNode*>(array.begin(), array.begin()+mid));
        treeHead->right = sortedArrayToBST(vector<ListNode*>(array.begin()+mid+1, array.end()));
        return treeHead;
    }
};