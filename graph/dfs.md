DFS
DFS
DFS
auto dfs$0 = [&](auto&& self, ll node, ll par) -> void {

    fora(g[node], child){
        if (child == par) continue;
        self(self, child, node);
    }
    
};
dfs$0(dfs$0, 1, 0);