Graph Input
gin
Takes graph of n nodes and m edges as input (bidirectional)
I(n, m);
vvl g(n+1);

forn(m){
    I(u, v);
    g[u].pb(v);
    g[v].pb(u);
}