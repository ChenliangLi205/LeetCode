class Solution {
public:
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        if(nums.size() <= 1) return true;
        if(k==1) return true;
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if(sum%k!=0) return false;
        int target = sum/k;
        sort(nums.begin(), nums.end(), greater<int>());
        if(nums[0] > target) return false;
        vector<int> groups(k,0);
        return helper(nums, target, groups, 0);
    }
    
    bool helper(vector<int>& nums, int target, vector<int>& groups, int currIdx){
        if(currIdx == nums.size()){
            for(int i: groups)
                if(i!=target) return false;
            return true;
        }
        else{
            for(int j=0;j<groups.size();j++){
                if(groups[j] + nums[currIdx] > target) continue;
                groups[j] += nums[currIdx];
                if(helper(nums, target, groups, currIdx+1)) return true;
                groups[j] -= nums[currIdx];
            }
            return false;
        }
    }
};