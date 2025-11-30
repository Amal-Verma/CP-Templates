treedpvec
treedpvec
treedpvec
auto treeDP = [&]<typename T = vl, typename R = ll>() -> vc<R> {

    T extra;
    auto add = [&](ll node) -> void {
        
    };

    auto remove = [&](ll node) -> void {

    };

    auto getans = [&](ll node) -> R {

    };

    auto adddfs = [&](auto&& self, ll node, ll par) -> void {
        add(node);
        fora(g[node], child){
            if (child == par) continue;
            self(self, child, node);
        }
    };

    auto removedfs = [&](auto&& self, ll node, ll par) -> void {
        remove(node);
        fora(g[node], child){
            if (child == par) continue;
            self(self, child, node);
        }
    };
    

    vc<R> dp = vc<R>(n+1);
    vl sz = vl(n+1, 1ll);
    
    auto dfssz = [&](auto&& self, ll node, ll par) -> void {
        fora(g[node], child){
            if (child == par) continue;
            self(self, child, node);
            sz[node] += sz[child];
        }
    };
    dfssz(dfssz, 1, 0);

    auto dfs = [&](auto&& self, ll node, ll par, bool keep) -> void {
        ll mx = -1, bigChild = -1;
        fora(g[node], child){
            if (child == par) continue;
            if (CMAX(mx, sz[child])) bigChild = child;
        }
        fora(g[node], smallchild){
            if (smallchild == par || smallchild == bigChild) continue;
            self(self, smallchild, node, false);
        }
        if (bigChild != -1) self(self, bigChild, node, true);

        fora(g[node], child){
            if (child == par || child == bigChild) continue;
            adddfs(adddfs, child, node);
        }

        add(node);
        dp[node] = getans(node);

        if (!keep){
            removedfs(removedfs, node, par);
        }
    };

    dfs(dfs, 1, 0, true);

    rt dp;
};

auto dp = treeDP();