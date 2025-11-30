Binary Search
bs
Binary Search FFFFTTTTT find first T in l
auto f = [&](ll m) -> bool {
    rt  0;
};

ll l = 0, r =1e18, m;
while((r-l) > 1){
    m = (r-l) / 2 + l;
    if (f(m)) r = m;
    else l = m;
}
if (!f(l)) l = r;
