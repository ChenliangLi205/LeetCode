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
    ListNode* oddEvenList(ListNode* head) {
        if(head == NULL) return head;
        if(head->next == NULL) return head;
        if(head->next->next == NULL) return head;
        ListNode* oddPtr = head;
        ListNode* evenPtr = head->next;
        ListNode* evenHead = evenPtr;
        while(true)
        {
            if(evenPtr->next == NULL)
            {
                oddPtr->next = evenHead;
                break;
            }
            oddPtr->next = evenPtr->next;
            oddPtr = oddPtr->next;
            evenPtr->next = oddPtr->next;
            evenPtr = evenPtr->next;
            if(oddPtr->next == NULL)
            {
                oddPtr->next = evenHead;
                break;
            }
        }
        return head;
    }
};