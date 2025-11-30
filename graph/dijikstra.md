Dijkstra
dijkstra
Dijkstra
using state = tuple<ll,ll>; 
ll start = 1;
vl dis = vec(n+1, inf);
dis[start] = 0;
priority_queue<state, vc<state>, greater<>> pq;
pq.emplace(0, start);

while(len(pq)){
    auto [d, x] = pq.top();
    pq.pop();

    if (dis[x] != d)
    continue;

    for(const auto& [y, w]: g[x]){
        if (dis[y] > (dis[x] + w)){
            dis[y] = dis[x] + w;
            pq.emplace(dis[y], y);
        }
    }
}
