#include <iostream>
#include <vector>
#include <algorithm>

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
    sort(arr, arr+n);
    cout << endl;
    cout << *max_element(arr, arr+3);
    cout << endl;
    // for(auto it=arr.begin(); it != arr.end(); it++) {
    //     cout << *it << ' ';
    // }
    for(int i=0; i< n; i++) 
        cout << arr[i] << ' ';
}