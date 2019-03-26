class Solution {
public:
    string getHint(string secret, string guess) {
        if(secret.size()==0) return "0A0B";
        map<char, int> num2cnt;
        set<int> bullsIdx;
        for(char c: secret)
        {
            if(num2cnt.find(c)==num2cnt.end()) num2cnt[c] = 0;
            num2cnt[c]++;
        }
        int A = 0;
        for(int i=0;i<guess.size();i++)
        {
            if(guess[i] == secret[i]) 
            {
                A++;
                num2cnt[guess[i]]--;
                bullsIdx.insert(i);
            }
        }
        int B = 0;
        for(int i=0;i<guess.size();i++)
        {
            if(bullsIdx.find(i)!= bullsIdx.end()) continue;
            if(num2cnt.find(guess[i])!=num2cnt.end() && num2cnt[guess[i]]>0)
            {
                num2cnt[guess[i]]--;
                B++;
            }
        }
        return to_string(A)+'A'+to_string(B)+'B';
    }
};