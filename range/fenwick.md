Fenwick Tree
Fenwick
Fenwick Tree
class Fenwick{
    public:
    ll n;
    vl BIT;

    void update(ll x, ll idx){
        idx++;
        for(;idx <= n;idx+=idx&-idx){
            BIT[idx] += x;
        }
    }

    ll query(ll idx){
        ll res = 0;
        idx++;
        for(;idx > 0; idx-=idx&-idx){
            res += BIT[idx];
        }
        rt res;
    }

    Fenwick(vl& ve){
        n = len(ve);
        BIT = vec(n+1, 0ll);
        forn(n){
            update(ve[i], i);
        }
    }

    Fenwick(ll m){
        n = m;
        BIT = vec(n+1, 0ll);
    }
};