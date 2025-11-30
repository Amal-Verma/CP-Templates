treedp
treedp
treedp
auto treeDP = [&]<typename T = set<ll>, typename R = ll>() -> vc<R> {

    auto merge = [&](T& a, const T& b) -> void {

    };

    auto base = [&](ll idx) -> T {

    };

    auto get = [&](T& a) -> R {

    };

    vc<R> dp = vc<R>(n+1);
    vl sz = vl(n+1, 1ll);
    vc<T> extra = vc<T>(n+1);

    forn(i, 1, n+1){
        extra[i] = move(base(i));
    }

    auto dfs = [&](auto&& self, ll node, ll par) -> void {
    
        fora(g[node], child){
            if (child == par) continue;
            self(self, child, node);
            sz[node] += sz[child];
        }

        ll max_sz = 0;
        ll heavy = -1;
        fora(g[node], child){
            if (child == par) continue;
            if (CMAX(max_sz, sz[child])){
                heavy = child;
            }
        }
        
        if (heavy != -1){
            swap(extra[node], extra[heavy]);
            fora(g[node], child){
                if (child == par || child == heavy) continue;
                merge(extra[node], extra[child]);
            }
            merge(extra[node], extra[heavy]);
        }

        dp[node] = get(extra[node]);
    };

    dfs(dfs, 1, 0);
    rt dp;
};

auto dp = treeDP();