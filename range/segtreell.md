Segment Tree (long long)
segll
Segment Tree <long long> class
class SegTree {
public:
    vector<ll> seg;
    ll size;
    function<ll(const ll&, const ll&)> combine;

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
        if (low == high) {
            seg[idx] = u;
            return;
        }
        ll mid = (low + high) / 2;
        if (k <= mid) update(2*idx+1, low, mid, k, u);
        else update(2*idx+2, mid+1, high, k, u);
        seg[idx] = combine(seg[2*idx+1], seg[2*idx+2]);
    }

    SegTree(const vl& ve, function<ll(const ll&, const ll&)> f) : combine(f) {
        size = ve.size();
        seg.resize(4*size);
        build(ve, 0, 0, size-1);
    }

    ll query(ll l, ll r) {
        return query(0, 0, size-1, l, r).F;
    }

    void update(ll k, ll u) {
        update(0, 0, size-1, k, u);
    }
};