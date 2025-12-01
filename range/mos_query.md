Mo's Offline Query
moquery
Mo's Offline Query Template
ll NSQRT = sqrt(n);
ll queries[q][4];

forn(i, q){
    I(l, r);
    l--, r--;
    queries[i][0] = l / NSQRT;
    queries[i][1] = r;
    queries[i][2] = l;
    queries[i][3] = i;
}

sort(queries, queries + q,
    [](auto& a, auto& b){
        if (a[0] != b[0]) return a[0] < b[0];
        if (a[0] & 1) return a[1] > b[1];
        if (a[1] == b[1]) return a[2] < b[2];
        return a[1] < b[1];
    }
);

ll ans = 0;

auto add_idx = [&](ll idx){

};

auto remove_idx = [&](ll idx){

};

vl out(q);
ll left = 0;
ll right = -1;
fora(queries, qq){
    while(right < qq[1]) add_idx(++right);
    while(right > qq[1]) remove_idx(right--);
    while(left > qq[2])  add_idx(--left);
    while(left < qq[2]) remove_idx(left++);
    out[qq[3]] = ans;
}    

