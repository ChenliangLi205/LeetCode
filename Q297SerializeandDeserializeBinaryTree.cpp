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
        if(root == NULL) return "";
        vector<string> val_str;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            TreeNode* tmp = q.front();
            q.pop();
            if(tmp == NULL) val_str.push_back("#");
            else{
                val_str.push_back(to_string(tmp->val));
                q.push(tmp->left);
                q.push(tmp->right);
            }
        }
        string s = "";
        for(string str: val_str){
            s += str;
            s += ",";
        }
        return s;
    }

    vector<string> split(string source, char par){
        vector<string> res;
        if(source.size() == 0) return res;
        string tmp = "";
        int len = 0;
        for(char c: source){
            if(c == par){
                res.push_back(tmp);
                tmp = "";
                len = 0;
            }
            else{
                tmp.insert(len, 1, c);
                len += 1;
            }
        }
        return res;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if(data.size() == 0) return NULL;
        if(data == "#") return NULL;
        vector<string> val_strs = split(data, ',');
        queue<TreeNode*> exposed;
        queue<bool> lefts;
        TreeNode* root = new TreeNode(atoi(val_strs[0].c_str()));
        exposed.push(root);
        lefts.push(true);
        for(int i=1;i<val_strs.size();i++){
            if(val_strs[i] == "#"){
                if(lefts.front())
                    lefts.front() = false;
                else
                {lefts.pop(); exposed.pop();}
            }
            else{
                TreeNode* newNode = new TreeNode(atoi(val_strs[i].c_str()));
                if(lefts.front()){
                    exposed.front()->left = newNode;
                    lefts.front() = false;
                }
                else{
                    exposed.front()->right = newNode;
                    lefts.pop();
                    exposed.pop();
                }
                exposed.push(newNode);
                lefts.push(true);
            }
        }
        return root;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));