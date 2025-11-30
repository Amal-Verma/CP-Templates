Subset Convo
subsetconvo
Subset Convolution
void zetat(vl& ve, int n){
    int k = __lg(n);
    
    forn(k)
    forn(mask, n)
    if ((mask >> i) & 1)
    ve[mask] += ve[mask ^ (1<<i)];
}

void mobioust(vl& ve, int n){
    int k = __lg(n);
    
    forn(k)
    forn(mask, n)
    if ((mask >> i) & 1)
    ve[mask] -= ve[mask ^ (1<<i)];
}

vl subset_convo(vl& f, vl& g){
    int n = len(f);
    int k = __lg(n);

    // ll F[k][n] = {0};
    // ll G[k][n] = {0};
    // ll H[k][n] = {0};
    vvl F = vec(k, n, 0ll);
    vvl G = vec(k, n, 0ll);
    vvl H = vec(k, n, 0ll);

    forn(mask, n){
        int bit = __builtin_popcount(mask);
        F[bit][mask] = f[mask];
        G[bit][mask] = g[mask];
    }

    forn(k){
        zetat(F[i], n);
        zetat(G[i], n);
    }

    
    forn(mask, n)
    forn(k + 1)
    forn(j, k + 1 - i)
    H[i + j][mask] += F[i][mask] * G[j][mask];

    forn(k)
    mobioust(H[i], n);

    vl h(n, 0);
    forn(mask, n)
    h[mask] = H[__builtin_popcountll(mask)][mask];

    rt h;
}