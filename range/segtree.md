Segment Tree 
seg
Segment Tree class
class SegTree {
public:
    vector<ll$0> seg;
    ll size;

    function<ll$0(const ll$0&, const ll$0&)> combine;

    void build(const vector<ll$0>& ve, ll idx, ll low, ll high) {
        if (low == high) {
            seg[idx] = ve[low];
            return;
        }
        ll mid = (low + high) / 2;
        build(ve, 2*idx+1, low, mid);
        build(ve, 2*idx+2, mid+1, high);
        seg[idx] = combine(seg[2*idx+1], seg[2*idx+2]);
    }

    pair<ll$0, bool> query(ll idx, ll low, ll high, ll l, ll r) {
        if (l <= low && r >= high) return pair(seg[idx], true);
        if (l > high || r < low) return pair(ll$0(), false);

        ll mid = (low + high) / 2;
        pair<ll$0, bool> left = query(2*idx+1, low, mid, l, r);
        pair<ll$0, bool> right = query(2*idx+2, mid+1, high, l, r);

        if (!left.S) return right;
        else if (!right.S) return left;

        return pair(combine(left.F, right.F), true);
    }

    void update(ll idx, ll low, ll high, ll k, ll$0 u) {
        if (low == high) {
            seg[idx] = u;
            return;
        }
        ll mid = (low + high) / 2;
        if (k <= mid) update(2*idx+1, low, mid, k, u);
        else update(2*idx+2, mid+1, high, k, u);
        seg[idx] = combine(seg[2*idx+1], seg[2*idx+2]);
    }

    SegTree(const vc<ll$0>& ve, function<ll$0(const ll$0&, const ll$0&)> f) : combine(f) {
        size = ve.size();
        seg.resize(4*size);
        build(ve, 0, 0, size-1);
    }

    ll$0 query(ll l, ll r) {
        return query(0, 0, size-1, l, r).F;
    }

    void update(ll k, ll$0 u) {
        update(0, 0, size-1, k, u);
    }
};
