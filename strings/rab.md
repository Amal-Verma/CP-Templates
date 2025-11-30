Rabin Karb
rab
Class to get polynomial hash of substring of a string in O(1) with O(n) precompute
class rab{
    public:
    static vvl prepp;
    static vl p;
    static vl m;
    static ll hshcnt;
    static ll RABMAX;
    static bool init;

    ll n;
    vvl pre;
    
    rab(str& s){
        if (!init){
            hshcnt = len(p);
            preppCal();
            init = true;
        }
        cal(s);
    };
    
    static void preppCal(){
        prepp = move(vec(RABMAX, hshcnt, 1ll));
        
        forn(i, 1, RABMAX){
            forn(h, hshcnt){
                prepp[i][h] = (prepp[i-1][h] * p[h]) % m[h];
            }
        }
    };
    
    ll mpp(char& c){
        if (c >= 'a' && c <= 'z') rt c - 'a'+1;
        if (c >= 'A' && c <= 'Z') rt c - 'A'+27;
    }
    
    void cal(str& s){
        n = len(s);
        pre = move(vec(n+1, hshcnt, 0ll));

        forn(n){
            forn(h, hshcnt){
                pre[i+1][h] = (pre[i][h] + mpp(s[i]) * prepp[i][h]) % m[h];
            }
        }
    }

    vl gethash(ll i, ll j){
        vl out(hshcnt);

        forn(h, hshcnt)
        out[h] = (((pre[j+1][h] - pre[i][h] + m[h])%m[h]) * prepp[n-i][h]) % m[h];

        rt out;
    }

    vl gethash(str& s){
        vl out(hshcnt);

        forn(len(s))
        forn(h, hshcnt)
        out[h] = (out[h] + (mpp(s[i]) * prepp[i][h]) % m[h]) % m[h];

        forn(h, hshcnt)
        out[h] = (out[h] * prepp[n][h]) % m[h];

        rt out;
    }
};

vvl rab::prepp;
vl rab::p = {31, 37, 53};
vl rab::m = {1000000007, 1000000009, 998244353};
ll rab::hshcnt;
ll rab::RABMAX = 1e6+100;
bool rab::init = false;