class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        if(nums.size() <= 1) return nums.size();
        if(nums.size() == 2)
        {
            if(nums[1]==nums[0]) return 1;
            else return 2;
        }
        vector<int> dp_goes_down(nums.size(), 1);
        vector<int> dp_goes_up(nums.size(), 1);
        for(int i=1;i<nums.size();++i)
        {
            for(int j=0;j<i;++j)
            {
                if(nums[i] > nums[j])
                {
                    dp_goes_up[i] = dp_goes_up[i] < dp_goes_down[j]+1 ?
                        dp_goes_down[j]+1 : dp_goes_up[i];
                }
                else if(nums[i] < nums[j])
                {
                    dp_goes_down[i] = dp_goes_down[i] < dp_goes_up[j]+1 ?
                        dp_goes_up[j]+1 : dp_goes_down[i];
                }
                else
                {
                    dp_goes_down[i] = dp_goes_down[i] < dp_goes_down[j] ?
                        dp_goes_down[j] : dp_goes_down[i];
                    dp_goes_up[i] = dp_goes_up[i] < dp_goes_up[j] ?
                        dp_goes_up[j] : dp_goes_up[i];
                }
            }
        }
        return dp_goes_up.back() > dp_goes_down.back()
            ? dp_goes_up.back() : dp_goes_down.back();
    }
};