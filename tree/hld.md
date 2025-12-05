HLD
HLD
HLD
template<typename T, typename Fn>
class HLD{
    public:
    ll n, curpos;
    vl sizes, depths, parent, heavy, pos, head;
    Fn combine;
    SegTree<T, Fn>* segtree;
    vc<T> ovals;

    void dfsPrecompute1(vvl& g, ll node, ll par){
        parent[node] = par;
        sizes[node] = 1;
        depths[node] = depths[par] + 1;
        fora(g[node], child){
            if (child == par) continue;
            dfsPrecompute1(g, child, node);
            sizes[node] += sizes[child];
            if (sizes[child] > sizes[heavy[node]]) heavy[node] = child;
        }
    };

    void dfsPrecompute2(vvl& g, ll node, ll h){
        head[node] = h;
        pos[node] = curpos++;
        if (heavy[node] != 0) {
            dfsPrecompute2(g, heavy[node], h);
        }
        fora(g[node], child){
            if (child == parent[node] || child == heavy[node]) continue;
            dfsPrecompute2(g, child, child);
        }
    };

    void precompute(vvl& g){
        n = len(g);
        sizes = vec(n, 1ll);
        depths = vec(n, 0ll);
        parent = vec(n, 0ll);
        heavy = vec(n, 0ll);
        pos = vec(n, 0ll);
        head = vec(n, 0ll);
        dfsPrecompute1(g, 1, 1);
        
        curpos = 0;
        dfsPrecompute2(g, 1, 1);
    };

    void update(ll node, T val){
        segtree->update(pos[node], val);
    };

    T query(ll a, ll b){
        T res;
        bool first = true;
        while (head[a] != head[b]){
            if (depths[head[a]] < depths[head[b]]) swap(a, b);
            if (first){
                res = segtree->query(pos[head[a]], pos[a]);
                first = false;
            } else {
                res = combine(res, segtree->query(pos[head[a]], pos[a]));
            }
            a = parent[head[a]];
        }

        if (depths[a] > depths[b]) swap(a, b);
        if (first){
            res = segtree->query(pos[a], pos[b]);
        } else {
            res = combine(res, segtree->query(pos[a], pos[b]));
        }

        return res;
    };
    
    void seginit(const vc<T>& vals){
        ovals = vec(n-1, T());
        forn(i, 1, n){
            ovals[pos[i]] = vals[i-1];
        }
    };
    
    HLD(vvl& g,const vc<T>& vals, Fn f): combine(f) {
        precompute(g);
        seginit(vals);
        segtree = new SegTree<T, Fn>(ovals, combine);
    }
    
    HLD(vvl& g,const vc<T>& vals, Fn f, T IDENTITY): combine(f) {
        precompute(g);
        seginit(vals);
        segtree = new SegTree<T, Fn>(ovals, combine, IDENTITY);
    }

    ~HLD(){
        delete segtree;
    }
};

template<typename T, typename Fn>
HLD(vvl&, const vc<T>&, Fn) -> HLD<T, Fn>;

template<typename T, typename Fn>
HLD(vvl&, const vc<T>&, Fn, T) -> HLD<T, Fn>;