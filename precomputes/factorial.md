Factorial
fact
Precomputes Factorial
vl fact;
void factorial(ll N){
    fact = move(vec(N, 1ll));
    forn(i, 1, N)
    fact[i] = (fact[i-1] * (i%M)) % M;
}