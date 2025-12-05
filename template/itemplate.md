Interactive Question Template
ipp
Interactive Question Template
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