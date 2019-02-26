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
    ListNode* MeetNode(ListNode* head){
        if(head == nullptr) return nullptr;
        if(head->next == nullptr) return nullptr;
        if(head->next->next == nullptr) return nullptr;
        
        ListNode* pSlow = head;
        ListNode* pFast = head->next;
        ListNode* meet = nullptr;
        
        while(pFast->next != nullptr && pFast->next->next != nullptr)
        {
            if(pSlow == pFast)
            {
                meet = pSlow;
                break;
            }
            pSlow = pSlow->next;
            pFast = pFast->next->next;
        }
        return meet;
    }
    
    int CycleLen(ListNode* start){
        if(start == nullptr) return 0;
        int len = 1;
        ListNode* pMove = start->next;
        
        while(pMove != start && pMove != nullptr)
        {
            pMove = pMove->next;
            len++;
        }
        if(pMove == nullptr) return 0;
        else return len;
    }
    
    
    ListNode *detectCycle(ListNode *head) {
        if(head == nullptr) return nullptr;
        ListNode* meet = MeetNode(head);
        if(meet == nullptr) return nullptr;
        int cycleLen = CycleLen(meet);
        if(cycleLen == 0) return nullptr;
        
        ListNode* pSlow = head;
        ListNode* pFast = head;
        for(int i=0;i<cycleLen;i++)
        {
            pFast = pFast->next;
            if(pFast == nullptr) return nullptr;
        }
        while(pFast != pSlow)
        {
            if(pFast == nullptr || pSlow == nullptr)
                return nullptr;
            pFast = pFast -> next;
            pSlow = pSlow -> next;
        }
        return pFast;
    }
};