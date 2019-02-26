class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        if(nums.size() <= 1) return;
        if(nums.size() == 2) {
            swap(nums[0], nums[1]);
            return;
        }
        bool r = false;
        queue<int> q;
        int i = nums.size()-1;
        q.push(nums.back());
        while(i>0)
        {
            if(nums[i-1] >= nums[i])
            {
                q.push(nums[i-1]);
            }
            else
            {
                break;
            }
            i--;
        }
        
        if(i==0)
        {
            int i_ = 0;
            while(!q.empty())
            {
                nums[i_] = q.front();
                q.pop();
                i_++;
            }
        }
        else
        {
            int i_ = i;
            bool swapped = false;
            while(!q.empty())
            {
                if(q.front() > nums[i-1] && !swapped)
                {
                    int tmp = nums[i-1];
                    nums[i-1] = q.front();
                    nums[i_] = tmp;
                    swapped = true;
                    i_++;
                    q.pop();
                }
                else
                {
                    nums[i_] = q.front();
                    q.pop();
                    i_++;
                }
            }
        }
        return;
    }
};