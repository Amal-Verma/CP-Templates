Primitive Root
primitiveroot
Primitive Root
ll primitive_root(ll m) {
    ll phi = m - 1;  // works for prime m
    ll n = phi;

    vector<ll> factors;
    for (ll i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            factors.push_back(i);
            while (n % i == 0) n /= i;
        }
    }
    if (n > 1) factors.push_back(n);

    for (ll g = 2; g < m; g++) {
        bool ok = true;
        for (ll p : factors) {
            if (binExp(g, phi / p, m) == 1) {
                ok = false;
                break;
            }
        }
        if (ok) return g;
    }
    return -1; // should not happen for valid m
}