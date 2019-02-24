/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if(root == NULL) return "#";
        string s = std::to_string(root->val);
        s.append(",");
        s.append(serialize(root->left));
        s.append(",");
        s.append(serialize(root->right));
        return s;
    }

    vector<string> split(string s, const char c){
        vector<string> v;
        string tmp="";
        if(s.size() == 0) return v;
        for(char s_char: s){
            if(s_char == c){
                v.push_back(tmp);
                tmp = "";
            }
            else tmp.push_back(s_char);
        }
        return v;
    }
    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if(data.size() == 0) return NULL;
        if(data == "#") return NULL;
        vector<string> v = split(data, ',');
        stack<TreeNode*> exposed;
        stack<bool> lefts;
        TreeNode* head = new TreeNode(atoi(v[0].c_str()));
        exposed.push(head);
        lefts.push(true);
        for(int i=1;i<v.size();i++){
            if(v[i] == "#"){
                if(lefts.top()) lefts.top() = false;
                else {exposed.pop();lefts.pop();}
                continue;
            }
            TreeNode* currNode = new TreeNode(atoi(v[i].c_str()));
            TreeNode* lastNode = exposed.top();
            if(lefts.top()){
                lastNode->left = currNode;
                lefts.top() = false;
            }
            else{
                lastNode->right = currNode;
                exposed.pop();
                lefts.pop();
            }
            exposed.push(currNode);
            lefts.push(true);
        }
        return head;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));