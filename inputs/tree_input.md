Tree input 
tin
Take tree of n nodes
I(n);
vvl g(n+1);

forn(n-1){
    I(u, v);
    g[u].pb(v);
    g[v].pb(u);
}