struct Interval_{
    int start;
    int end;
    Interval_(int s, int e):start(s), end(e){}
    string out(){
        return start==end? to_string(start): to_string(start)+"->"+to_string(end);
    }
};

class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> ans;
        if(nums.size()==0) return ans;
        vector<Interval_> inters;
        for(int i: nums){
            if(inters.empty() || inters.back().end != i-1) inters.push_back(Interval_(i,i));
            else inters.back().end = i;
        }
        for(Interval_ i: inters) ans.push_back(i.out());
        return ans;
    }
};