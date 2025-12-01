SparseTable
SparseTable
SparseTable
template<typename T, typename Fn>
class SparseTable {
    private:
    vvc<T> sparse;
    Fn combine;
    ll n;
    ll logn;

    public:

    void build(const vc<T>& ve) {
        forn(i, n) sparse[0][i] = ve[i];
        forn(j, 1, logn) {
            forn(i, n - (1 << j) + 1) {
                sparse[j][i] = combine(sparse[j-1][i], sparse[j-1][i + (1 << (j-1))]);
            }
        }
    }

    T query(ll l, ll r) {
        ll j = __lg(r - l + 1);
        rt combine(sparse[j][l], sparse[j][r - (1 << j) + 1]);
    }

    SparseTable(const vector<T>& ve, Fn f) : combine(move(f)) {
        n = len(ve);
        logn = __lg(n) + 1;
        sparse = vec(logn, n, T());
        build(ve);
    }
};
template<typename T, typename Fn>
SparseTable(const vector<T>&, Fn) -> SparseTable<T, Fn>;