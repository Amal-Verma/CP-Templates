DSU
DSU
DSU
class DSU {
    private: 
    vl parent, size;

    public:
    DSU(ll n) {
        parent = vec(n, 0ll);
        size = vec(n, 1ll);
        forn(n) parent[i] = i;
    }

    ll find(ll a) {
        if (parent[a] == a) return a;
        return parent[a] = find(parent[a]);
    }

    bool unite(ll a, ll b) {
        a = find(a);
        b = find(b);
        if (a == b) return false;
        if (size[a] < size[b]) swap(a, b);
        parent[b] = a;
        size[a] += size[b];
        return true;
    }

    ll getSize(ll a) {
        return size[find(a)];
    }

    bool same(ll a, ll b) {
        rt find(a) == find(b);
    }
};