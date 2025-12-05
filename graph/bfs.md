BFS
BFS
BFS
auto bfs$0 = [&](ll start){
    vc<bool> visited(n+1, -1);
    queue<ll> q;

    visited[start] = 1;
    q.push(start);

    while(len(q)){
        ll node = q.front();
        q.pop();

        fora(g[node], child){
            if (!visited[child]){
                visited[child] = 1;
                q.push(child);
            }
        }
    }
}
bfs$0(1);