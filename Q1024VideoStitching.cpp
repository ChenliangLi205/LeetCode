#define MAXINT 0x7ffffffe

class Solution {
public:
    static bool clipSmaller(vector<int>& v1, vector<int>& v2)
    {
        return v1[0] < v2[0];
    }
    
    int videoStitching(vector<vector<int>>& clips, int T) {
        if(clips.empty()) return -1;
        vector<int> dp(T+1, MAXINT);
        int left,right;
        sort(clips.begin(), clips.end(), clipSmaller);
        if(clips[0][0] > 0) return -1;
        dp[0] = 0;
        for(vector<int> v : clips)
        {
            left = v[0];
            right = v[1];
            if(left > T) break;
            if(dp[left] == MAXINT) return -1;
            for(int i=left+1;i<=right&&i<=T;i++)
            {
                dp[i] = dp[i] < dp[left]+1 ? dp[i] : dp[left]+1;
            }
        }
        if(dp.back() == MAXINT) return -1;
        else return dp.back();
    }
};