struct DListNode
{
    int val;
    DListNode* prev;
    DListNode* next;
    DListNode(int x): val(x), prev(nullptr), next(nullptr) {}
    DListNode(int x, DListNode* p): val(x), prev(p), next(nullptr) {}
};

class MinStack {
public:
    /** initialize your data structure here. */
    DListNode* tail;
    DListNode* head;
    int currMin;
    
    MinStack() {
        tail = nullptr;
        head = nullptr;
        currMin = 0x7fffffff;
    }
    
    void push(int x) {
        if(head==nullptr)
        {
            head = new DListNode(x);
            currMin = x;
            tail = head;
        }
        else
        {
            if(x < currMin)
                currMin = x;
            tail->next = new DListNode(x, tail);
            tail = tail->next;
        }
    }
    
    void pop() {
        if(head==nullptr)
            return;
        if(head==tail)
        {
            currMin = 0x7fffffff;
            head = nullptr;
            tail = nullptr;
            return;
        }
        if(tail->val == currMin)
        {
            currMin = 0x7fffffff;
            for(DListNode* curr = head;curr != tail; curr = curr->next)
                currMin = currMin < curr->val? currMin: curr->val;
        }
        tail = tail->prev;
    }
    
    int top() {
        if(head==nullptr)
            return 0;
        return tail->val;
    }
    
    int getMin() {
        return currMin;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */