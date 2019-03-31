# define INF 0x7fffffff

class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        if(n<=1) return 1;
        if(primes.size()==0) return 1;
        vector<int> indices;
        for(int p: primes) indices.push_back(0);
        vector<int> uglyNumbers;
        uglyNumbers.push_back(1);
        while(uglyNumbers.size() < n)
        {
            int minVal = INF;
            int minIdx = 0;
            for(int i=0;i<primes.size();i++)
            {
                int nextVal = uglyNumbers[indices[i]] * primes[i];
                if(nextVal < minVal)
                {
                    minVal = nextVal;
                    minIdx = i;
                }
            }
            indices[minIdx]++;
            if(minVal != uglyNumbers.back())
                uglyNumbers.push_back(minVal);
        }
        return uglyNumbers.back();
    }
};