#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

vector<int> insertion_sort(vector<int> ar) {
    int i, j, hole, curr;
    for(i=0; i<ar.size(); i++) {
        if(i == 0) continue;
        hole = i;
        curr = ar[hole];
        for(j=i-1; j>=0 && ar[j] >= curr; j--) {
            ar[j+1] = ar[j];
        }
        ar[j+1] = curr;
    }
    return ar;
}
bool freq_compare(pair<int, int> p1, pair<int, int> p2) {
    // Check the frequency 
    // if frequency is same, check the values of pairs
    return(p1.second > p2.second || (p1.second == p2.second && p1.first < p2.first));
}

void sort_by_frequency(int arr[], int n) {
    unordered_map<int, int> hash;
    int i;

    // Creating frequency map in hash 
    for(i=0; i<n; i++) {
        if(hash.find(arr[i]) != hash.end())
            hash[arr[i]]++;
        else
            // hash.insert(make_pair(arr[i], 1));
            hash[arr[i]] = 1;
    }

    // For sorting the map - copy it to vector
    vector <pair<int, int>> freq;
    for(auto it=hash.begin(); it != hash.end(); it++)
        freq.push_back(make_pair(it->first, it->second));
    // sorting the new vector
    sort(freq.begin(), freq.end(), freq_compare);
    // Rearranging array elements
    int k=0;
    for(int i=0; i<freq.size(); i++) {
        for(int j=0; j<freq[i].second; j++)
            arr[k++] = freq[i].first;
    }
}

int main() {
    // vector<int> arr;
    int arr[20];
    int n, input;
    cin >> n;
    for(int i=0; i<n && cin >> input; i++) {
        // arr.push_back(input);
        arr[i] = input;
    }
    // arr = insertion_sort(arr);
    // sort(arr, arr+n);
    sort_by_frequency(arr, n);
    cout << endl;
    cout << *max_element(arr, arr+3);
    cout << endl;
    // for(auto it=arr.begin(); it != arr.end(); it++) {
    //     cout << *it << ' ';
    // }
    for(int i=0; i< n; i++) 
        cout << arr[i] << ' ';
}