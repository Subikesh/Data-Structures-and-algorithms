#include <iostream>
#include <map>

using namespace std;

void iterate(map<int, int> mp) {
    for (auto ite = mp.begin(); ite != mp.end(); ite++)
        cout << ite->first << '\t' << ite->second << endl;
}

int main() {
    map<int, int> smap1;
    smap1.insert(pair<int, int>(3, 50));
    smap1.insert(pair<int, int>(4, 1000));
    smap1.insert(pair<int, int>(1, 5));
    smap1.insert(pair<int, int>(-4, 20));
    smap1.insert(pair<int, int>(10, 9));

    iterate(smap1);
    // cout << smap1.find(20)->first << '\t' << smap1.find(20)->second;
    // cout << smap1.end()->first << '\t' << smap1.end()->second;
    int num;
    map<int, int>::iterator itr;
    cin >> num;
    // Retrieve an element from map - use find()
    // If element not present in map - it returns map.end() iterator
    if((itr = smap1.find(num)) == smap1.end())
        cout << "Nope";
    else
        cout << "Here it is : " << itr->first << '\t' << itr->second;
    return 0;
}