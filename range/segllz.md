Segment Tree (long long) with lazy propagation
segllz
Segment Tree <long long> class with lazy propagation
class SegTree {
public:
    vector<ll> seg;
    vector<ll> lz1;
    vector<pair<ll, bool>> lz2;
    ll size;

    inline ll combine(const ll& a,const ll& b){
        return a + b;
    }

    void lzp1(ll idx, ll low, ll high){
        if (!lz1[idx]) rt;
        seg[idx] += lz1[idx] * (high - low + 1);
        
        if (low != high){
            lz1[2*idx+1] += lz1[idx];
            lz1[2*idx+2] += lz1[idx];
        }
        lz1[idx] = 0;
    }

    void lzp2(ll idx, ll low, ll high){
        if (!lz2[idx].S) rt;
        seg[idx] = lz2[idx].F* (high - low + 1);

        if (low != high){
            lz2[2*idx+1] = lz2[idx];
            lz2[2*idx+2] = lz2[idx];
            lz1[2*idx+1] = 0;
            lz1[2*idx+2] = 0;
        }
        lz2[idx].S = false;
    }

    void lzp(ll idx, ll low, ll high){  
        lzp2(idx, low, high);
        lzp1(idx, low, high);
    }

    void build(const vector<ll>& ve, ll idx, ll low, ll high) {
        if (low == high) {
            seg[idx] = ve[low];
            return;
        }
        ll mid = (low + high) / 2;
        build(ve, 2*idx+1, low, mid);
        build(ve, 2*idx+2, mid+1, high);
        seg[idx] = combine(seg[2*idx+1], seg[2*idx+2]);
    }

    pair<ll, bool> query(ll idx, ll low, ll high, ll l, ll r) {
        lzp(idx, low, high);
        if (l <= low && r >= high) return pair(seg[idx], true);
        if (l > high || r < low) return pair(0, false);

        ll mid = (low + high) / 2;
        pair<ll, bool> left = query(2*idx+1, low, mid, l, r);
        pair<ll, bool> right = query(2*idx+2, mid+1, high, l, r);

        if (!left.S) return right;
        else if (!right.S) return left;

        return pair(combine(left.F, right.F), true);
    }

    void update(ll idx, ll low, ll high, ll k, ll u) {
        lzp(idx, low, high);
        if (low == high) {
            seg[idx] = u;
            return;
        }
        ll mid = (low + high) / 2;
        if (k <= mid) update(2*idx+1, low, mid, k, u);
        else update(2*idx+2, mid+1, high, k, u);
        seg[idx] = combine(seg[2*idx+1], seg[2*idx+2]);
    }

    void rangeinc(ll idx, ll low, ll high, ll l, ll r, ll x){
        lzp(idx, low, high);
        if (l <= low && r >= high){
            lz1[idx] += x;
            lzp(idx, low, high);
            rt;
        }
        if (l > high || r < low) return;

        ll mid = (low + high) / 2;
        rangeinc(2*idx+1, low, mid, l, r, x);
        rangeinc(2*idx+2, mid+1, high, l, r, x);
        seg[idx] = combine(seg[2*idx+1], seg[2*idx+2]);
    }

    void rangeset(ll idx, ll low, ll high, ll l, ll r, ll x){
        lzp(idx, low, high);
        if (l <= low && r >= high){
            lz2[idx] = {x, true};
            lz1[idx] = 0;
            lzp(idx, low, high);
            rt;
        }
        if (l > high || r < low) return;

        ll mid = (low + high) / 2;
        rangeset(2*idx+1, low, mid, l, r, x);
        rangeset(2*idx+2, mid+1, high, l, r, x);
        seg[idx] = combine(seg[2*idx+1], seg[2*idx+2]);
    }

    SegTree(const vc<ll>& ve) {
        size = ve.size();
        seg.resize(4*size);
        lz1.resize(4*size);
        lz2.resize(4*size);
        build(ve, 0, 0, size-1);
    }

    ll query(ll l, ll r) {
        return query(0, 0, size-1, l, r).F;
    }

    void update(ll k, ll u) {
        update(0, 0, size-1, k, u);
    }

    void rangeinc(ll l, ll r, ll x){
        rangeinc(0, 0, size-1, l, r, x);
    }

    void rangeset(ll l, ll r, ll x){
        rangeset(0, 0, size-1, l, r, x);
    }
};
