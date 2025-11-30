Compress vector
compressvec
Compress vector ve
auto comp = ve;
sort(all(comp));
comp.erase(unique(all(comp)), comp.end());
for (auto& x : ve)
x = lower_bound(all(comp), x) - comp.begin();