binary lifting
blift
Output binary lifting vector
ll ulg = __lg(n)+1;
vvl up = move(vec(n, ulg, 0ll));

auto blift = [&](auto&& self, ll node, ll par) -> void {
    up[node][0] = par;
    
    fora(g[node], c){
        if (c == par) continue;
        self(self, c, node);
    }

};
blift(blift, 1, 0);

forn(i, 1, ulg){
    forn(node, 1, n)
    up[node][i] = up[up[node][i-1]][i-1];
}