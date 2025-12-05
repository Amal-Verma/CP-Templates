seg
seg
seg
using segNodeType = ll;
inline segNodeType segIDENTITY = 0;

inline segNodeType segCombine(const segNodeType& a, const segNodeType& b) {
    rt a + b;
}

template<typename T>
inline segNodeType segCreateNode(T x) {
    rt x;
}

template<typename T>
class SegTree {
public:
    vc<segNodeType> seg;
    ll n;

    void build(const vector<T>& ve) {
        forn(i, n) seg[n + i] = segCreateNode(ve[i]);
        forrn(i, n-1, 0) seg[i] = segCombine(seg[i<<1], seg[i<<1 | 1]);
    }

    void update(ll pos, T value) {
        for(seg[pos += n] = segCreateNode(value); pos >>= 1;) seg[pos] = segCombine(seg[pos<<1], seg[pos<<1 | 1]);
    }

    segNodeType query(ll l, ll r) {
        segNodeType resl = segIDENTITY, resr = segIDENTITY;
        for(l += n, r += n + 1; l < r; l >>= 1, r >>= 1) {
            if (l & 1) resl = segCombine(resl, seg[l++]);
            if (r & 1) resr = segCombine(seg[--r], resr);
        }
        rt segCombine(resl, resr);
    }

    SegTree(const vc<T>& ve){
        n = len(ve);
        seg.resize(2*n);
        build(ve);
    }
};