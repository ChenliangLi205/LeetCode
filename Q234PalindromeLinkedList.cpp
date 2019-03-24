/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if(head == nullptr||head->next==nullptr) return true;
        vector<int> s;
        while(head!=nullptr){
            s.push_back(head->val);
            head = head->next;
        }
        int left=0, right=s.size()-1;
        while(left<right){
            if(s[left++] != s[right--]) return false;
        }
        return true;
    }
};