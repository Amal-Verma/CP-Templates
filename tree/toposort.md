Topological Sort
toposort
Output toposort array for graph g
vl topa;
auto topo = [&](){
    ll n = len(g);
    topa.clear();
    vector<bool> vis(n, false);
    auto dfs = [&](auto&& self, ll node, ll par) -> void {
        if (vis[node]) rt;
        vis[node] = true;
        fora(g[node], c){
            if (c == par) continue;
            self(self, c, node);
        }
        topa.pb(node);
    };

    forn(i, 1, n)
    dfs(dfs, i, i);

    reverse(all(topa));
};
topo();