Low Sieve
lowsi
Precompute Low Sieve
vl lo;
vl primes;

void losieve(ll siN){
    lo = move(vec(siN+1, 0ll));

    forn(siN+1)
    lo[i] = i;

    for(int i = 2; i <= siN; i++){
        if (lo[i] == i) primes.pb(i);
        fora(primes, x){
            if (i*x >= siN) break;
            lo[i * x] = x;
            if (!(i % x)) break;
        }
    }
}

vpl factorise(ll x){
    vpl factors;
    while(x > 1){
        ll cnt = 0;
        ll p = lo[x];
        while(!(x%p)){
            x /= p;
            cnt++;
        }
        factors.pb({p, cnt});
    }
    rt factors;
}