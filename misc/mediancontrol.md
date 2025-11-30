MedianControl
MedianControl
MedianControl
template<typename T = ll>
class MedianControl {
    private:
    multiset<T> low;
    multiset<T> high;

    public:
    
    void balance() {
        if (low.size() > high.size() + 1) {
            high.insert(*low.rbegin());
            low.erase(--low.end());
        } else if (high.size() > low.size()) {
            low.insert(*high.begin());
            high.erase(high.begin());
        }
    }

    void insert(T value) {
        if (low.empty() || value <= *low.rbegin()) {
            low.insert(value);
        } else {
            high.insert(value);
        }
        balance();
    }

    void remove(T value) {
        if (!low.empty() && value <= *low.rbegin()) {
            low.erase(low.find(value));
        } else {
            high.erase(high.find(value));
        }
        balance();
    }

    T get_median() {
        T median;
        if (low.size() > high.size()) {
            median = *low.rbegin();
        } else {
            median = (*low.rbegin() + *high.begin()) / 2;
        }
        rt median;
    }

    MedianControl() {
        
    }
};