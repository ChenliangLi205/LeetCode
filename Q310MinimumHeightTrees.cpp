# define INF 0x3f3f3f3f

class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<pair<int, int>>& edges) {
        vector<int> ans;
        if(n==0) return ans;
        ans.push_back(0);
        if(n==1) return ans;
        ans.push_back(1);
        if(edges.size() == 1) return ans;
        
        ans.clear();
        vector<int> node2degree;
        vector<vector<int>> leaves;
        vector<set<int>> node2nodes;
        for(int i=0;i<n;i++)
        {
            node2degree.push_back(0);
            node2nodes.push_back(set<int>());
        }
        for(pair<int,int> edge : edges)
        {
            int u = edge.first;
            int v = edge.second;
            node2degree[u]++;
            node2degree[v]++;
            node2nodes[u].insert(v);
            node2nodes[v].insert(u);
        }
        set<int> roots;
        for(int i=0;i<n;i++) roots.insert(i);
        vector<int> leavesThisRound;
        while(roots.size()>1)
        {
            for(int i=0;i<n;i++)
            {
                if(node2degree[i] == 1)
                {
                    node2degree[i]--;
                    leavesThisRound.push_back(i);
                }   
            }
            leaves.push_back(leavesThisRound);
            for(int i: leavesThisRound)
            {
                roots.erase(i);
                for(int j: node2nodes[i])
                    node2degree[j]--;
            }
            leavesThisRound.clear();
        }
        if(roots.size()==1)
            ans.push_back(*roots.begin());
        else
            ans = leaves.back();
        return ans;
    }
    
};