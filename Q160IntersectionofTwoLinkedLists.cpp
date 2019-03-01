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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if(headA == nullptr || headB == nullptr)
            return nullptr;
        stack<ListNode*> sa;
        stack<ListNode*> sb;
        ListNode* currA = headA;
        ListNode* currB = headB;
        while(currA!=nullptr)
        {
            sa.push(currA);
            currA = currA -> next;
        }
        while(currB!=nullptr)
        {
            sb.push(currB);
            currB = currB -> next;
        }
        ListNode* a = nullptr;
        ListNode* b = nullptr;
        while(!sa.empty() && !sb.empty())
        {
            if(sa.top() != sb.top())
                return a;
            a = sa.top();
            b = sb.top();
            sa.pop();
            sb.pop();
        }
        return a;
    }
};