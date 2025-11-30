FWHT
FWHT
FWHT
void FWHT(vl& a, bool inv) {
	for (int n = len(a), step = 1; step < n; step *= 2) {
		for (int i = 0; i < n; i += 2 * step) 
        forn(j, i, i+step) {
			ll &u = a[j], &v = a[j + step]; tie(u, v) =
				inv ? pl(v - u, u) : pl(v, u + v); // AND
				// inv ? pl(v, u - v) : pl(u + v, u); // OR /// include-line
				// pl(u + v, u - v);                   // XOR /// include-line
		}
	}
	// if (inv) for (ll& x : a) x /= len(a); // XOR only /// include-line
}
vl conv(vl a, vl b) {
    int N = 1;
    while (N < max(len(a), len(b))) N <<= 1;
    a.resize(N);
    b.resize(N);
    
	FWHT(a, 0); FWHT(b, 0);
	forn(i, 0,len(a)) a[i] *= b[i];
	FWHT(a, 1); return a;
}