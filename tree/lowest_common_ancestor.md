Lowest Common Ancestor of tree
lca
Get lca of two nodes in O(logn)
ll ulg = __lg(n)+1;
vvl up = move(vec(n, ulg, 0ll));
vl tin(n+1, -1), tout(n+1, -1);
ll timer;

auto blift = [&](auto&& self, ll node, ll par) -> void {
    tin[node] = timer;
    up[node][0] = par;
    
    fora(g[node], c){
        if (c == par) continue;
        self(self, c, node);
    }

    tout[node] = timer;
};
blift(blift, 1, 0);

forn(i, 1, ulg){
    forn(node, 1, n)
    up[node][i] = up[up[node][i-1]][i-1];
}

tin[0] = -inf;
tout[0] = inf;
auto ancestor = [&](ll u, ll v){
    rt (tin[u] <= tin[v] && tout[u] >= tout[v]);
};

auto lca = [&](ll u, ll v){
    if (ancestor(u, v)) rt u;
    if (ancestor(v, u)) rt v;

    forrn(i, ulg-1){
        if (!ancestor(up[u][i], v))
        u = up[u][i];
    }
    rt up[u][0];
};