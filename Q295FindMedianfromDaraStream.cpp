class MedianFinder {
private:
    vector<int> list;
public:
    /** initialize your data structure here. */
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        if(list.size()==0) list.push_back(num);
        else{
            int idx = bisect(num);
            list.insert(list.begin()+idx, num);
        }
    }
    
    double findMedian() {
        if(list.size() % 2 == 0)
        {
            int idx1 = list.size()/2;
            int idx2 = list.size()/2-1;
            return (double)(list[idx1]+list[idx2]) / (double)2;
        }
        else
        {
            int idx = list.size() / 2;
            return (double)list[idx];
        }
    }
    
    int bisect(int n)
    {
        if(list.size()==0) return 0;
        if(list.size()==1) return n>list[0]? 1: 0;
        int left=0;
        int right = list.size();
        int mid = (left+right) / 2;
        while(left<right){
            if(list[mid] == n) return mid;
            if(list[mid] < n) left=mid+1;
            else right=mid;
            mid = (left+right)/2;
        }
        return left;
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */