Inverse from 1 to N
invs
Precompute inverse from 1 to N
vl inv;
void inverse(ll N){
    inv = move(vec(N, 0ll));
    forn(i, N)
    inv[i] = ModInv(i);
}