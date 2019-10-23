class Solution {
public:
    bool oneMutation(string ori, string tar)
    {
        size_t cnt=0;
        for(size_t i=0;i<8;++i)
            if(ori[i]!=tar[i]) cnt++;
        return cnt == 1;
    }
    
    int minMutation(string start, string end, vector<string>& bank) {
        int mutation_cnt=0;
        vector<string> cur_genes, next_genes;
        
        next_genes.push_back(start);
        while(!next_genes.empty())
        {
            cur_genes = move(next_genes);
            next_genes.clear();
            for(string cur_gene: cur_genes)
            {
                if(cur_gene == end) return mutation_cnt;
                for(auto it=bank.begin();it!=bank.end();)
                {
                    if(oneMutation(cur_gene, *it))
                    {
                        next_genes.push_back(*it);
                        it = bank.erase(it);
                    }
                    else ++it;
                }
            }
            mutation_cnt++;
        }
        return -1;
    }
};