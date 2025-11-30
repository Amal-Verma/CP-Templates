NTT
ntt
NTT
const long long MOD = 998244353;
const long long G = 3; // primitive root

void ntt(vl & a, bool invert) {
    int n = len(a);

    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) swap(a[i], a[j]);
    }

    for (int len = 2; len <= n; len <<= 1) {
        ll wlen = binExp(G, (MOD - 1) / len, MOD);
        if (invert) wlen = binExp(wlen, MOD - 2, MOD);

        for (int i = 0; i < n; i += len) {
            ll w = 1;
            for (int j = 0; j < len/2; j++) {
                ll u = a[i + j];
                ll v = ModMul(a[i + j + len/2], w, MOD);

                a[i + j] = ModAdd(u, v, MOD);
                a[i + j + len/2] = ModSub(u, v, MOD);

                w = ModMul(w, wlen, MOD);
            }
        }
    }

    if (invert) {
        ll inv_n = binExp(n, MOD - 2, MOD);
        foru(a, x) cModMul(x, inv_n, MOD);
    }
}

vl multiply(vl a, vl b) {
    int n = 1;
    while (n < len(a) + len(b)) n <<= 1;
    a.resize(n);
    b.resize(n);

    ntt(a, false);
    ntt(b, false);

    forn(i, 0, n)
    a[i] = a[i] * b[i] % MOD;

    ntt(a, true);

    return a;
}