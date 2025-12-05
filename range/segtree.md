Segment Tree 
segrec
Segment Tree class
template<typename K, typename Fn1, typename Fn2>
class SegTree {
public:
    ll size;
    Fn1 combine;
    Fn2 createNode;

    using T = decltype(std::declval<Fn2>()(std::declval<K>()));
    vector<T> seg;

    void build(const vector<K>& ve, ll idx, ll low, ll high) {
        if (low == high) {
            seg[idx] = move(createNode(ve[low]));
            return;
        }
        ll mid = (low + high) / 2;
        build(ve, 2*idx+1, low, mid);
        build(ve, 2*idx+2, mid+1, high);
        seg[idx] = combine(seg[2*idx+1], seg[2*idx+2]);
    }

    pair<T, bool> query(ll idx, ll low, ll high, ll l, ll r) {
        if (l <= low && r >= high) return {seg[idx], true};
        if (l > high || r < low) return {T(), false};

        ll mid = (low + high) / 2;
        pair<T, bool> left = query(2*idx+1, low, mid, l, r);
        pair<T, bool> right = query(2*idx+2, mid+1, high, l, r);

        if (!left.S) return right;
        else if (!right.S) return left;

        return {combine(left.F, right.F), true};
    }

    void update(ll idx, ll low, ll high, ll k, K u) {
        if (low == high) {
            seg[idx] = move(createNode(u));
            return;
        }
        ll mid = (low + high) / 2;
        if (k <= mid) update(2*idx+1, low, mid, k, u);
        else update(2*idx+2, mid+1, high, k, u);
        seg[idx] = combine(seg[2*idx+1], seg[2*idx+2]);
    }

    SegTree(const vc<K>& ve, Fn1 f, Fn2 g = Identity<K>{}) : combine(f), createNode(g) {
        size = ve.size();
        seg.resize(4*size);
        build(ve, 0, 0, size-1);
    }

    T query(ll l, ll r) {
        return query(0, 0, size-1, l, r).F;
    }

    void update(ll k, K u) {
        update(0, 0, size-1, k, u);
    }
};
template<typename K, typename Fn1>
SegTree(const vc<K>&, Fn1) -> SegTree<K, Fn1, decltype(Identity<K>{})>;