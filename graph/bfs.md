BFS
BFS
BFS
auto bfs = [&](ll start){
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