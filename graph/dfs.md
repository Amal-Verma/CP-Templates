DFS
DFS
DFS
auto dfs = [&](auto&& self, ll node, ll par) -> void {

    fora(g[node], child){
        if (child == par) continue;
        self(self, child, node);
    }
    
};
dfs(dfs, 1, 0);