class WordDictionary {
private:
    struct TrieNode{
        TrieNode* kids[26];
        bool endsHere;
        TrieNode(): endsHere(false)
        {
            for(int i=0;i<26;i++)
                kids[i] = nullptr;
        }
    };
    TrieNode* head;
public:
    /** Initialize your data structure here. */
    WordDictionary() {
        head = new TrieNode();
    }
    
    /** Adds a word into the data structure. */
    void addWord(string word)
    {
        if(word.size() == 0) return;
        TrieNode* currNode = head;
        for(char c: word)
        {
            if(currNode->kids[c-'a'] == nullptr)
                currNode->kids[c-'a'] = new TrieNode();
            currNode = currNode->kids[c-'a'];
        }
        currNode->endsHere = true;
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    bool search(string word)
    {
        if(word.size() == 0) return false;
        vector<TrieNode*> possible; 
        vector<TrieNode*> newPossible;
        possible.push_back(head);
        for(char c: word)
        {
            if(c=='.')
            {
                for(auto node: possible)
                {
                    for(int i=0;i<26;i++)
                    {
                        if(node->kids[i]!=nullptr)
                            newPossible.push_back(node->kids[i]);
                    }
                }
            }
            else
            {
                for(auto node: possible)
                {
                    if(node->kids[c-'a']!=nullptr)
                        newPossible.push_back(node->kids[c-'a']);
                }
            }
            if(newPossible.size()==0) return false;
            possible = newPossible;
            newPossible.clear();
        }
        for(auto node: possible)
        {
            if(node->endsHere) return true;
        }
        return false;
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * bool param_2 = obj.search(word);
 */