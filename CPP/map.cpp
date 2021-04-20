#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

void iterate(map<string, int> mp) {
    for (auto ite = mp.begin(); ite != mp.end(); ite++)
        cout << ite->first << '\t' << ite->second << endl;
    cout << endl;
}

bool compare_pairs(const pair<int, int> p1, const pair<int, int> p2) {
    return (p1.second < p2.second);
}

int main() {
    map<string, int> smap1 = {{"1", 50},{"4", 28},{"2", 5},{"6", 20},{"10", 9}};
    iterate(smap1);

    smap1["6"] = 40;
    smap1["10"] = 50;
    iterate(smap1);
    cout << endl;
    // vector<pair<int, int>> vec;

	/* // Declaring priority_queue with custom comparator
    auto compare = [](int lhs, int rhs)
                {
                    return lhs < rhs;
                };

    std::priority_queue<int, std::vector<int>, decltype(compare)> q(compare);
    (or)
    struct CustomCompare
    {
        bool operator()(const int& lhs, const int& rhs)
        {
            return lhs < rhs;
        }
    };
    std::priority_queue<int, std::vector<int>, CustomCompare> pq;
    */
    return 0;
}