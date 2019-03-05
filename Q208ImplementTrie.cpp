class Trie {
private:
    struct TrieNode{
        TrieNode* kids[26];
        bool someWordEndsHere;
        TrieNode(): someWordEndsHere(false){
            for(int i=0;i<26;i++)
                kids[i] = nullptr;
        }
    };
    TrieNode* head;
public:
    /** Initialize your data structure here. */
    Trie() {
        head = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        if(word.size() == 0) return;
        TrieNode* currNode = head;
        for(char c: word)
        {
            if(currNode->kids[c-'a'] == nullptr)
                currNode->kids[c-'a'] = new TrieNode();
            currNode = currNode->kids[c-'a'];
        }
        currNode->someWordEndsHere = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        if(word.size()==0) return true;
        TrieNode* currNode = head;
        for(char c: word)   
        {
            if(currNode->kids[c-'a'] == nullptr) return false;
            currNode = currNode->kids[c-'a'];
        }
        if (currNode->someWordEndsHere) return true;
        else return false;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        if(prefix.size() == 0) return true;
        TrieNode* currNode = head;
        for(char c: prefix)
        {
            if(currNode->kids[c-'a'] == nullptr) return false;
            currNode = currNode->kids[c-'a'];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * bool param_2 = obj.search(word);
 * bool param_3 = obj.startsWith(prefix);
 */