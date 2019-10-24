class Solution {
public:
    bool match(const vector<string>& pattern_lows, const string& pattern_high, const vector<string>& target_lows, const string& target_high)
    {
        if(pattern_high != target_high) return false;
        for(size_t i=0 ; i<pattern_lows.size() ; ++i)
        {
            if(!lowerCharMatch(pattern_lows[i], target_lows[i]))
                return false;
        }
        return true;
    }
    
    void splitLowHigh(string& s, vector<string>& lows, string& high)
    {
        string low;
        for(char c: s)
        {
            if(c >= 'A' && c <= 'Z')
            {
                high.push_back(c);
                lows.push_back(low);
                low.clear();
            }
            else low.push_back(c);
        }
        lows.push_back(low);
        return;
    }
    
    bool lowerCharMatch(const string& pattern, const string& target)
    {
        size_t i = 0;
        bool find = false;
        for(char c: pattern)
        {
            for(;i<target.size();++i)
            {
                if(target[i] == c)
                {
                    find=true;
                    ++i;
                    break;
                }
            }
            if(!find) return false;
            find=false;
        }
        return true;
    }
    
    vector<bool> camelMatch(vector<string>& queries, string pattern) {
        vector<bool> res;
        vector<string> p_lows, t_lows;
        string p_high, t_high;
        splitLowHigh(pattern, p_lows, p_high);
        for(string s : queries)
        {
            t_lows.clear();
            t_high.clear();
            splitLowHigh(s, t_lows, t_high);
            res.push_back(match(p_lows, p_high, t_lows, t_high));
        }
        return res;
    }
};