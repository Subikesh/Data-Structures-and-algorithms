#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

void iterate(map<int, int> mp) {
    for (auto ite = mp.begin(); ite != mp.end(); ite++)
        cout << ite->first << '\t' << ite->second << endl;
}

bool compare_maps(const pair<int, int> m1, const pair<int, int> m2) {
    return (m1.second < m2.second);
}

int main() {
    map<int, int> smap1 = {{1, 50},{4, 28},{2, 5},{6, 20},{10, 9}};
    iterate(smap1);
    cout << endl;
    vector<pair<int, int>> vec;

	// copy key-value pairs from the map to the vector
    for (auto it2=smap1.begin(); it2!=smap1.end(); it2++) 
    {
        vec.push_back(make_pair(it2->first, it2->second));
    }
    sort(vec.begin(), vec.end(), compare_maps);
    // iterate(vec);
    for(auto it2 = vec.begin(); it2!= vec.end(); it2++)
        cout << it2->first << '\t' << it2->second << endl;
    // cout << smap1.find(20)->first << '\t' << smap1.find(20)->second;
    // cout << smap1.end()->first << '\t' << smap1.end()->second;
    // string num;
    // map<string, string>::iterator itr;
    // cin >> num;
    // // Retrieve an element from map - use find()
    // // If element not present in map - it returns map.end() iterator
    // if((itr = smap1.find(num)) == smap1.end())
    //     cout << "Nope";
    // else
    //     cout << "Here it is : " << itr->first << '\t' << itr->second;
    return 0;
}