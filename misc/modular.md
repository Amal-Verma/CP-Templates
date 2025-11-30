Modular Arithmetic
mm
Modular Arithmetic
ll binExp(ll a, ll b, ll mod = M,ll ans=1) {
    for (; b; b >>= 1, a = a * a % mod)
        if (b & 1) ans = a * ans % mod;
    rt ans;
}

inline ll ModAdd(ll a, ll b, ll m = M) { rt ((a % m) + (b % m)) % m; }
inline ll ModSub(ll a, ll b, ll m = M) { rt ((a % m) - (b % m) + m) % m; }
inline ll ModMul(ll a, ll b, ll m = M) { rt ((a % m) * (b % m)) % m; }
inline ll ModInv(ll a, ll m = M) { rt binExp(a, M - 2, M); }
inline ll ModDiv(ll a, ll b, ll m = M) { rt ModMul(a, ModInv(b, m), m); }

inline void cModAdd(ll& a, ll b, ll m = M) { a = ((a % m) + (b % m)) % m; }
inline void cModSub(ll& a, ll b, ll m = M) { a = ((a % m) - (b % m) + m) % m; }
inline void cModMul(ll& a, ll b, ll m = M) { a = ((a % m) * (b % m)) % m; }
inline void cModDiv(ll& a, ll b, ll m = M) { a = ModMul(a, ModInv(b, m), m); }
inline void cModInv(ll& a, ll m = M) { a = binExp(a, M - 2, M); }