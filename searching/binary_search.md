Binary Search
bs
Binary Search FFFFTTTTT finds breakpoint
auto bs$0 = [&](ll l = 0, ll r = 1e18) -> pl {
    // FFFTTT finds breakpoint
    auto f = [&](ll m) -> bool {
        rt  false;
    };
    
    ll m;
    while((r-l) > 1){
        m = (r-l) / 2 + l;
        if (f(m)) r = m;
        else l = m;
    }

    rt {l, r};
};
pl interbs$0 = bs$0();