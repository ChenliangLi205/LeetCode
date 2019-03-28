struct BListNode
{
    int val;
    BListNode* next;
    BListNode* prev;
    BListNode(int v):val(v), next(nullptr), prev(nullptr){}
};
class RandomizedSet {
private:
    unordered_map<int, BListNode*> val2node;
    BListNode* head;
    BListNode* tail;
    int numVals;
public:
    /** Initialize your data structure here. */
    RandomizedSet() {
        head = nullptr;
        tail = nullptr;
        numVals = 0;
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if(val2node.find(val)!=val2node.end()) return false;
        else
        {
            if(head == nullptr)
            {
                head = new BListNode(val);
                tail = head;
                
            }
            else
            {
                tail->next = new BListNode(val);
                tail->next->prev = tail;
                tail = tail->next;
            }
            val2node.insert({val, tail});
            numVals++;
            return true;
        }
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if(numVals == 0) return false;
        auto it = val2node.find(val);
        if(it==val2node.end()) return false;
        else
        {
            auto to_delete = it->second;
            if(to_delete == head)
            {
                if(numVals == 1)
                {
                    head = nullptr;
                    tail = nullptr;
                }
                else
                {
                    head->next->prev = nullptr;
                    head = head->next;
                }
            }
            else if(to_delete == tail)
            {
                tail = tail->prev;
            }
            else
            {
                to_delete->prev->next = to_delete->next;
                to_delete->next->prev = to_delete->prev;
            }
            val2node.erase(it);
            numVals--;
            return true;
        }
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        if(numVals == 0) return 0;
        if(numVals == 1) return head->val;
        int idx = rand() % numVals;
        BListNode* curr = head;
        for(int i=0;i<idx;i++) curr = curr->next;
        return curr->val;
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */