#define MAX_INT 0x7fffffff
class Solution {
public:
    vector<pair<int, int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<pair<int, int>> results;
        if(nums1.size()==0 || nums2.size()==0 || k<=0) return results;
        if(k>nums1.size()*nums2.size()) k=nums1.size()*nums2.size();
        results.push_back(pair<int, int>(nums1[0], nums2[0]));
        set<pair<int, int>> candidates;
        set<pair<int, int>> visited;
        visited.insert(pair<int,int>(0,0));
        if(nums2.size()>1)
        {candidates.insert(pair<int,int>(0,1));}
        if(nums1.size()>1)
        {candidates.insert(pair<int,int>(1,0));}
        int i;
        int big;
        pair<int, int> tmp;
        int idx1,idx2,big_idx1,big_idx2;
        set<pair<int,int>>::iterator it;
        pair<int,int> newCandidate;
        while(results.size() < k)
        {
            i=0;
            big= MAX_INT;
            big_idx1 = 0;
            big_idx2 = 0;
            it = candidates.begin();
            while(it!=candidates.end())
            {
                idx1 = it->first;
                idx2 = it->second;
                if(nums1[idx1]+nums2[idx2] < big)
                {
                    big = nums1[idx1]+nums2[idx2];
                    big_idx1 = idx1;
                    big_idx2 = idx2;
                }
                ++it;
            }
            candidates.erase(pair<int,int>(big_idx1, big_idx2));
            visited.insert(pair<int,int>(big_idx1, big_idx2));
            results.push_back(pair<int,int>(nums1[big_idx1], nums2[big_idx2]));
            newCandidate.first = big_idx1+1;
            newCandidate.second = big_idx2;
            if(visited.find(newCandidate) == visited.end() && big_idx1+1 < nums1.size())
            {candidates.insert(newCandidate);}
            newCandidate.first = big_idx1;
            newCandidate.second = big_idx2+1;
            if(visited.find(newCandidate) == visited.end() && big_idx2+1 < nums2.size())
            {candidates.insert(newCandidate);}
        }
        return results;
    }
};