matexpo
matexpo
matexpo
struct matrix{
    vvl mat;

    matrix operator*(const matrix& other){
        ll n = len(mat);
        ll m = len(other.mat[0]);
        ll p = len(other.mat);
        matrix res;
        res.mat = vec(n, m, 0ll);
        forn(i, n){
            forn(k, p){
                if (mat[i][k] == 0) continue;
                forn(j, m){
                    cModAdd(res.mat[i][j], ModMul(mat[i][k], other.mat[k][j]));
                }
            }
        }
        rt res;
    }

    matrix pow(ll b){
        ll n = len(mat);
        matrix res;
        res.mat = vec(n, n, 0ll);
        forn(i, n){
            res.mat[i][i] = 1;
        }
        matrix base = *this;
        for (; b; b >>= 1, base = base * base)
            if (b & 1) res = res * base;
        rt res;
    }
};