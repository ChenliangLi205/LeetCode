/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        vector< vector<int> > res;
        if(root == nullptr) return res;
        vector<Node*> cur,next;
        next.push_back(root);
        while(!next.empty())
        {
            cur = move(next);
            next.clear();
            vector<int> thisLevelVal;
            for(size_t i=0;i<cur.size();++i)
            {
                thisLevelVal.push_back(cur[i]->val);
                for(Node* child : cur[i]->children)
                    if(child!=nullptr) next.push_back(child);
            }
            res.push_back(thisLevelVal);
        }
        return res;
    }
};