class Solution {
public:
    bool isValidSerialization(string preorder) {
        if (preorder.size() == 0) return false;
        if (preorder.size() == 1)
        {
            if(preorder[0] == '#') return true;
            else return false;
        }
        if (preorder.size() > 1 && preorder[0] == '#') return false;
        vector<short> kidNum;
        kidNum.push_back(2);
        bool result=true;
        bool lastIsComma=false;
        for(int i=1;i<preorder.size();i++)
        {
            if(preorder[i] == ',') {lastIsComma=true;continue;}
            if(lastIsComma)
            {
                lastIsComma=false;
                if(kidNum.size()==0) {result=false;break;}
                kidNum[kidNum.size()-1] --;
                if(kidNum[kidNum.size()-1]==0) kidNum.pop_back();
                if(preorder[i] != '#') kidNum.push_back(2);
            }
        }
        if(kidNum.size()!=0) result=false;
        return result;
    }
};