#include <bits/stdc++.h>
/*
    Question here:
    https://www.youtube.com/watch?v=GBuHSRDGZBY&list=WL&index=1
    Given 2 unsorted array of same length. 
    Find the pair of elements from two arrays who's sum is closest to the given number  
*/

using namespace std;

pair<int, int> find_nearest(vector<int> arr1, vector<int> arr2, int n, int need) {
    pair<int, int> res(n-1, 0);
    int min_sum = INT_MAX, i=n-1, j=0, curr_sum;
    while(i>=0 && j<n) {
        curr_sum = arr1[i] + arr2[j];
        if(abs(curr_sum-need) < min_sum) {
            min_sum = abs(curr_sum-need);
            res = make_pair(i, j);
        }
        // cout << curr_sum << ' ' << min_sum <<` ' ' << i << ' ' << j << endl;
        if(curr_sum == need) {
            res = make_pair(i, j);
            break;
        }
        else if(curr_sum < need) {
            j++;
        }
        else {
            i--;
        }
    }
    return res;
}

int main() {
    vector<int> arr1, arr2;
    pair<int, int> res;
    int n, token, temp;
    cin >> n;
    for(int i=0; i<n; i++) {
        cin >> temp;
        arr1.push_back(temp);
    }
    for(int i=0; i<n; i++) {
        cin >> temp;
        arr2.push_back(temp);
    }
    cin >> token;
    res = find_nearest(arr1, arr2, n, token);
    cout << arr1[res.first] << ' ' << arr2[res.second];
    return 0;
}