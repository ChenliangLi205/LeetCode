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
    void reorderList(ListNode* head) {
        if(head == nullptr || head->next == nullptr || head->next->next == nullptr) return;
        stack<ListNode*> s;A
        ListNode* curr = head;
        while(curr!=nullptr)
        {
            s.push(curr);
            curr = curr->next;
        }
        curr = head;
        int target = s.size() / 2;
        for(int cnt = 0; cnt < target && curr!=nullptr ;cnt++)
        {
            ListNode* tmp = curr->next;
            curr->next = s.top();
            s.top()->next = tmp;
            s.pop();
            curr = tmp;
        }
        curr -> next = nullptr;
        return;
    }
};