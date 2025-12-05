NCR
ncr
NCR
vl fact;
void factorial(ll N){
    fact = move(vec(N, 1ll));
    forn(i, 1, N)
    fact[i] = (fact[i-1] * (i%M)) % M;
}

vl ifact;
void ifactorial(ll N){
    factorial(N);
    ifact = move(vec(N, 1ll));
    ifact[N-1] = ModInv(fact[N-1]);
    forrn(i, N-2)
    ifact[i] = ModMul(ifact[i+1], i+1);
}

inline ll ncr(ll n, ll r){
    rt ModMul(fact[n], ModMul(ifact[r], ifact[n-r]));
}