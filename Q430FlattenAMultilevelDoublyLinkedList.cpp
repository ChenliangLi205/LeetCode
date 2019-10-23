/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;

    Node() {}

    Node(int _val, Node* _prev, Node* _next, Node* _child) {
        val = _val;
        prev = _prev;
        next = _next;
        child = _child;
    }
};
*/
class Solution {
public:
    Node* flatten(Node* head) {
        if(head == nullptr) return head;
        Node* newHead = new Node(head->val, nullptr, nullptr, nullptr);
        Node* cur = head;
        Node* newCur = newHead;
        while(cur!=nullptr)
        {
            if(cur->child != nullptr)
            {
                newCur->next = flatten(cur->child);
                while(newCur->next!=nullptr)
                {
                    newCur->next->prev = newCur;
                    newCur = newCur->next;
                }
            }
            if(cur->next!=nullptr)
            {
                newCur->next = new Node(cur->next->val, nullptr, nullptr, nullptr);
                newCur->next->prev = newCur;
            }
            cur = cur->next;
            newCur = newCur->next;
        }
        return newHead;
    }
};