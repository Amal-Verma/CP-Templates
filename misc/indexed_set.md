Indexed Set
indst
import indexed set
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
template<typename T, typename Compare = less<T>>
using indexed_set = __gnu_pbds::tree<T, __gnu_pbds::null_type, Compare, __gnu_pbds::rb_tree_tag, __gnu_pbds::tree_order_statistics_node_update>;