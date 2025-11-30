Sieve
si
Precompute Sieve
vector<bool> si;
vl primes;

void sieve(ll siN){
    si = move(vec(siN+1, true));
    si[0] = si[1] = false;

    for(int i = 2; i <= siN; i++){
        if (si[i]) primes.pb(i);
        fora(primes, x){
            if (i*x >= siN) break;
            si[i * x] = false;
            if (!(i % x)) break;
        }
    }
}