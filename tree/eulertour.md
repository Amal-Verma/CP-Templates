eulertour
eulertour
eulertour
auto eulertour = [&](){
    vl tour;
    vl tin(n+1, -1), tout(n+1, -1);

    auto fn = [&](ll node, bool touting) -> ll {
        rt ve[node-1];
    };

    auto eulertourdfs = [&](auto&& self, ll node, ll par) -> void {
        
        tin[node] = len(tour);
        tour.pb(fn(node, false));
        fora(g[node], child){
            if (child == par) continue;
            self(self, child, node);
        }
        tout[node] = len(tour);
        tour.pb(fn(node, true));
        
    };
    eulertourdfs(eulertourdfs, 1, 0);

    return tuple(tour, tin, tout);
};
auto [tour, tin, tout] = eulertour();