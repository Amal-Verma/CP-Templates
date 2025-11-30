Distance nodes (a, b) in tree
tdis
Get Distance between 2 nodes in a tree in O(logn)
ll ulg = __lg(n)+1;
vvl up = move(vec(n + 1, ulg, 0ll));
vl tin(n+1, -1), tout(n+1, -1);
vl depth(n+1, inf);
ll timer;

auto blift = [&](auto&& self, ll node, ll par, ll dep) -> void {
    tin[node] = timer;
    up[node][0] = par;
    depth[node] = dep;

    fora(g[node], c){
        timer++;
        if (c != par)
        self(self, c, node, dep + 1);
    }

    tout[node] = timer;

};
blift(blift, 1, 0, 0);

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

    forrn(ulg-1, -1, i){
        if (!ancestor(up[u][i], v))
        u = up[u][i];
    }
    rt up[u][0];
};

auto getdis = [&](ll u, ll v){
    rt depth[u] + depth[v] - 2*depth[lca(u, v)];
};