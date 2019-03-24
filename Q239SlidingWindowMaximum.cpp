class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int left=0;
        int right=left+k;
        vector<int> ans;
        int lastMaxFromLeft=0;
        if(nums.size() ==0 || k==0) return ans;
        while(right<=nums.size())
        {
            if(!ans.empty() && !lastMaxFromLeft>0){
                int lastMax = ans.back();
                if(nums[right-1] < lastMax){
                    ans.push_back(lastMax);
                    lastMaxFromLeft--;
                }
                else{
                    ans.push_back(lastMax);
                    lastMaxFromLeft=k;
                }
            }
            else{
                int biggest = nums[left];
                lastMaxFromLeft = 1;
                for(int i=left+1;i<right;i++){
                    if(nums[i] >= biggest){
                        biggest = nums[i];
                        lastMaxFromLeft = i-left+1;
                    }
                }
                ans.push_back(biggest); 
            }
            left++;
            right++;
        }
        return ans;
    }
};