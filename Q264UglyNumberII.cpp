class Solution {
public:
    int smallest(int n1, int n2, int n3){
        int mid = n1 < n2? n1: n2;
        return mid < n3? mid: n3;
    }
    
    int nthUglyNumber(int n) {
        if(n<=1) return 1;
        int idx_2=0, idx_3=0, idx_5=0;
        vector<int> us;
        us.push_back(1);
        while(us.size()<n){
            int u2 = us[idx_2]*2;
            int u3 = us[idx_3]*3;
            int u5 = us[idx_5]*5;
            int min_ = smallest(u2,u3,u5);
            if(min_==u2) idx_2++;
            if(min_==u3) idx_3++;
            if(min_==u5) idx_5++;
            us.push_back(min_);
        }
        return us.back();
    }
};