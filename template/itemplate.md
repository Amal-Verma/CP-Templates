Interactive Question Template
ipp
Interactive Question Template
#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define endl '\n'
#define forn(start, end, var) for(ll var = (start); var < (end); ++var)
#define forrn(start, end, var) for(ll var = (start); var > (end); --var)
#define fora(v, var) for(const auto& var: (v))
#define foru(v, var) for(auto& var: (v))
#define rt return
#define F first
#define S second
#define all(v) (v).begin(), (v).end()
#define _sort(v) sort(all(v))
#define _rsort(v) sort((v).rbegin(), (v).rend())
#define sum(v) accumulate(all(v), 0ll)
#define len(x) ((int)(x.size()))
#define pb push_back
#define get_bit(x,i) (((x) >> (i)) & 1ll)
#define precision(x, p) std::cout << std::fixed << std::setprecision(p) << x << endl;

const ll M = 1000000007;
const ll inf = (ll)1e15;

template <typename C>
constexpr inline decltype(auto) ng(C&& container, int idx) noexcept {
    if (idx < 0) idx += (int)std::size(container);
    return std::forward<C>(container)[idx];
}

template<typename T> using vc = vector<T>;
template<typename T> using vvc = vc<vc<T>>;
template<typename T> using vvvc = vc<vvc<T>>;
template<typename T> using vvvvc = vc<vvvc<T>>;

using pl = pair<ll,ll>;
using vl = vc<ll>;
using vvl = vvc<ll>;
using vvvl = vvvc<ll>;
using vvvvl = vvvvc<ll>;
using vpl = vc<pl>;
using vvpl = vvc<pl>;
using vs = vc<string>;
using vvs = vvc<string>;

#ifdef ONLINE_JUDGE
#else
inline void pim(const ll& in,ostream& o,const string& s=""){
    if (in == inf) o<<"inf"<<s;
    else o<<in<<s;
}
#endif
template<typename T>
inline std::enable_if_t<std::is_arithmetic_v<T>>
pim(const T& in,ostream& o,const string& s = "") {o<<in<<s;}
inline void pim(const string& in,ostream& o,const string& s=""){o<<in<<s;}
template<typename T1,typename T2>
inline void pim(const std::pair<T1,T2>& p,ostream& o,const string& s=""){o<<'(';pim(p.first,o,", ");pim(p.second,o,")");o<<s;}
template<typename T>
typename std::enable_if<std::is_same<decltype(std::begin(std::declval<T>())),decltype(std::end(std::declval<T>()))>::value>::type
inline pim(const T& c,ostream& o,const string& s=""){
    ll n=c.size();
    if(&o == &cerr){o<<'[';fora(c,x){n--;pim(x,o,n?", ":"");}o<<"]";o<<s;}
    else{fora(c,x){n--;pim(x,o,n?" ":"");};o<<s;}
}
template<typename Fs,typename... R>
inline void pimr(ostream& o, const Fs& f,const R&... r){if constexpr(sizeof...(r)>0){pim(f,o," ");pimr(o,r...);}else{pim(f,o);o<<endl;}}

template<typename... args>
void print(const args&... r){pimr(cout, r...);}

struct custom_hash {
static uint64_t splitmix64(uint64_t x) {
    x += 0x9e3779b97f4a7c15;
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
    x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
    return x ^ (x >> 31);
}
size_t operator()(uint64_t x) const {
    static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
    return splitmix64(x + FIXED_RANDOM);
}
};
#ifdef ONLINE_JUDGE
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
#define um gp_hash_table
#define dbg(x...)
#else
#define um unordered_map
#define dbg(...) do { \
    cerr << "[" << #__VA_ARGS__ << "] = "; \
    pimr(cerr, __VA_ARGS__); \
    cerr.flush(); \
} while (0)
#endif
template<typename Key, typename Value, typename Hash = custom_hash>
using hm = um<Key, Value, Hash>;

template<typename T>
inline auto vvec(int n,T in){return vector(n, in);}
template<typename... Args>
inline auto vvec(int n, Args... args) {return vector(n, move(vvec(args...)));}
#define vec(...) std::move(vvec(__VA_ARGS__))

template<typename T>
inline void fill(T& x){cin >> x;}
template<typename T, typename L>
inline void fill(pair<T, L>& p){fill(p.F);fill(p.S);}
template<typename T>
inline void fill(vc<T>& v){foru(v, e)fill(e);}
template<typename... Args, typename T>
inline void fill(T& first, Args&... args) {fill(first);fill(args...);}

template<typename T>
inline T min(const vc<T>& v) {rt *min_element(all(v));}
template<typename T>
inline T max(const vc<T>& v) {rt *max_element(all(v));}

template<typename T>
inline int min_idx(const vc<T>& v){rt min_element(all(v))-v.begin();}
template<typename T>
inline int max_idx(const vc<T>& v){rt max_element(all(v))-v.begin();}

template<typename T, typename... Args>
constexpr inline T max(const T& a, const Args&... args) {
    return std::max({a, args...});
}
template<typename T, typename... Args>
constexpr inline T min(const T& a, const Args&... args) {
    return std::min({a, args...});
}

template<typename T, typename... Args>
inline void cmax(T& a, const Args&... b){ a = max(a, b...); }
template<typename T, typename... Args>
inline void cmin(T& a, const Args&... b){ a = min(a, b...); }

#define I(...) ll int __VA_ARGS__; fill(__VA_ARGS__)
#define STR(...) string __VA_ARGS__; fill(__VA_ARGS__)
#define V(x, ...) auto x = move(vec(__VA_ARGS__)); fill(x)

template<typename T, typename R>
inline void prc(bool con, const T& yes, const R& no){
    if (con) print(yes);
    else print(no);
}

template<typename T>
inline void pra(vc<T>& ve, ll l = 0, ll r = -1){
    if (r == -1) r = len(ve);
    forn(l, r, i) cout << ve[i] << " ";
    cout << endl;
}

using queryout = bool;

class Judge{
    public: 

    Judge(){
        // take judge input
    }

    template <typename... Args>
    queryout query(ll l, ll r) {
        
        rt queryout();
    }

    template <typename... Args>
    void found(const Args&... args) {
        print(args...);
    }
};

#ifdef ONLINE_JUDGE
template <typename... Args>
queryout qquery(const Args&... args) {
    print('?', args...);
    cout.flush();
    queryout x;
    cin >> x;
    rt x
}

template <typename... Args>
void ffound(const Args&... args) {
    print('!', args...);
    cout.flush();
}
#else
#define qquery(...) jjjjudge.query(__VA_ARGS__)
#define ffound(...) jjjjudge.found(__VA_ARGS__)
#endif


void precalc(){

}

void solve(){

    #ifdef ONLINE_JUDGE
    #else
    Judge jjjjudge;
    #endif


}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t=1;
    // cin>>t;
    precalc();
    while(t--){
        solve();
    }
    rt 0;
}