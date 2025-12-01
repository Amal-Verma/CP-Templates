Segment Tree 
seg
Segment Tree class
template<typename T, typename Fn>
class SegTree {
public:
    vector<T> seg;
    ll size;

    Fn combine;

    void build(const vector<T>& ve, ll idx, ll low, ll high) {
        if (low == high) {
            seg[idx] = ve[low];
            return;
        }
        ll mid = (low + high) / 2;
        build(ve, 2*idx+1, low, mid);
        build(ve, 2*idx+2, mid+1, high);
        seg[idx] = combine(seg[2*idx+1], seg[2*idx+2]);
    }

    pair<T, bool> query(ll idx, ll low, ll high, ll l, ll r) {
        if (l <= low && r >= high) return pair(seg[idx], true);
        if (l > high || r < low) return pair(T(), false);

        ll mid = (low + high) / 2;
        pair<T, bool> left = query(2*idx+1, low, mid, l, r);
        pair<T, bool> right = query(2*idx+2, mid+1, high, l, r);

        if (!left.S) return right;
        else if (!right.S) return left;

        return pair(combine(left.F, right.F), true);
    }

    void update(ll idx, ll low, ll high, ll k, T u) {
        if (low == high) {
            seg[idx] = u;
            return;
        }
        ll mid = (low + high) / 2;
        if (k <= mid) update(2*idx+1, low, mid, k, u);
        else update(2*idx+2, mid+1, high, k, u);
        seg[idx] = combine(seg[2*idx+1], seg[2*idx+2]);
    }

    SegTree(const vc<T>& ve, Fn f) : combine(move(f)) {
        size = ve.size();
        seg.resize(4*size);
        build(ve, 0, 0, size-1);
    }

    T query(ll l, ll r) {
        return query(0, 0, size-1, l, r).F;
    }

    void update(ll k, T u) {
        update(0, 0, size-1, k, u);
    }
};
template<typename T, typename Fn>
SegTree(const vc<T>&, Fn) -> SegTree<T, Fn>;