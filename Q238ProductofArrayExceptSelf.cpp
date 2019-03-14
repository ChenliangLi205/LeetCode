class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ans;
        if(nums.size()==0) return ans;
        ans.push_back(0);
        if(nums.size()==1) return ans;
        ans.pop_back();
        int already=1;
        for(int i=0;i<nums.size();i++)
        {
            ans.push_back(already);
            already *= nums[i];
        }
        already = 1;
        for(int i=nums.size()-1;i>=0;i--)
        {
            ans[i] *= already;
            already *= nums[i];
        }
        return ans;
    }
};