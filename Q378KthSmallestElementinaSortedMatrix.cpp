class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size();
        int* colSmall = new int[n];
        int* rowSmall = new int[n];
        for(int i=0;i<n;i++){
            colSmall[i] = n;
            rowSmall[i] = n;
        }
        int cnt=0;
        int result;
        set<pair<int,int>> candidates;
        candidates.insert(*new pair<int,int>(0,0));
        while(cnt<k){
            int smallest = 0x7fffffff;
            int smallRow=0;
            int smallCol=0;
            set<pair<int,int>>:: iterator small_ptr=candidates.begin();
            set<pair<int,int>>:: iterator it = candidates.begin();
            while(it!=candidates.end()){
                int r = it->first;
                int c = it->second;
                if(matrix[r][c] < smallest){
                    smallRow = r;
                    smallCol = c;
                    small_ptr = it;
                    smallest = matrix[r][c];
                }
                ++it;
            }
            candidates.erase(small_ptr);
            rowSmall[smallRow] = n;
            colSmall[smallCol] = n;
            if(smallRow+1<n && rowSmall[smallRow+1] > smallCol){
                candidates.insert(*new pair<int,int>(smallRow+1, smallCol));
            }
            if(smallCol+1<n && colSmall[smallCol+1] > smallRow){
                candidates.insert(*new pair<int,int>(smallRow, smallCol+1));
            }
            result = matrix[smallRow][smallCol];
            ++cnt;
        }
        return result;
    }
};