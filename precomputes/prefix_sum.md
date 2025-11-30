Prefix Sum
presum
Function to get Prefix sum
vl presum(vl& v){
    vl pre(1, 0);
    fora(v, e) pre.pb(pre.back() + e);
    rt pre;
}