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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        stack<int> s1;
        stack<int> s2;
        while(l1!=NULL){
            s1.push(l1->val);
            l1 = l1->next;
        }
        while(l2!=NULL){
            s2.push(l2->val);
            l2 = l2->next;
        }
        int bonus = 0;
        stack<int> res;
        while(!s1.empty() || !s2.empty()){
            if(!s1.empty() && !s2.empty()){
                int tmp = s1.top() + s2.top() + bonus;
                if(tmp < 10){
                    bonus = 0;
                    res.push(tmp);
                }
                else{
                    bonus=1;
                    res.push(tmp%10);
                }
                s1.pop();
                s2.pop();
                continue;
            }
            if(s1.empty()){
                int tmp = s2.top() + bonus;
                if(tmp<10){
                    bonus=0;
                    res.push(tmp);
                }
                else{
                    bonus=1;
                    res.push(tmp%10);
                }
                s2.pop();
                continue;
            }
            if(s2.empty()){
                int tmp = s1.top() + bonus;
                if(tmp<10){
                    bonus = 0;
                    res.push(tmp);
                }
                else{
                    bonus=1;
                    res.push(tmp%10);
                }
                s1.pop();
                continue;
            }
        }
        if(bonus == 1){res.push(bonus);}
        ListNode* head = new ListNode(res.top());
        ListNode* curr = head;
        res.pop();
        while(!res.empty()){
            curr->next = new ListNode(res.top());
            res.pop();
            curr = curr->next;
        }
        return head;
    }
};