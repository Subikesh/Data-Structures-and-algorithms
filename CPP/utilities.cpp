/* 
    Basic Utility functions in c++
*/

#include <iostream>
#include <vector>
#include <unordered_map>
// For string to int convertion
#include <sstream>
#include <algorithm>

using namespace std;

int is_prime(int n) {
    if(n == 1) return 0;
    if(n == 2) return 1;
    for (int i = 2; i*i <= n; i++)
        if (n%i == 0)
            return 0;
    return 1;
}

// swap two elements
void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

// Reverse an array
void reverse(int arr[], int n) {
    for (int i = 0; i < n/2; i++)
        swap(arr[i], arr[n-i-1]);
}

int is_vowel(char c) {
    if(c=='a' || c=='e' || c=='i' || c=='o' || c=='u' || c=='A' || c=='E' || c=='I' || c=='O' || c=='U')
        return 1;
    else
        return 0;
}

void insertion_sort(vector<int> &ar) {
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
}

bool freq_compare(pair<int, int> p1, pair<int, int> p2) {
    // Check the frequency 
    // if frequency is same, check the values of pairs
    return(p1.second > p2.second || (p1.second == p2.second && p1.first < p2.first));
}

void sort_by_frequency(int arr[], int n) {
    unordered_map<int, int> hash_map;
    int i;

    // Creating frequency map in hash_map 
    for(i=0; i<n; i++) {
        if(hash_map.find(arr[i]) != hash_map.end())
            hash_map[arr[i]]++;
        else
            // hash_map.insert(make_pair(arr[i], 1));
            hash_map[arr[i]] = 1;
    }

    // For sorting the map - copy it to vector
    vector <pair<int, int>> freq;
    for(int i=0; i<hash_map.size(); i++)
        freq.push_back(make_pair(arr[i], hash_map[arr[i]]));
    // sorting the new vector
    sort(freq.begin(), freq.end(), freq_compare);
    // Rearranging array elements
    int k=0;
    for(int i=0; i<freq.size(); i++) {
        for(int j=0; j<freq[i].second; j++)
            arr[k++] = freq[i].first;
    }
}

// Use stoi() instead 
// int convert_to_int(string str) {
//     stringstream convert(str);
//     int n;
//     convert >> n;
//     return n;
// }

int main() {
    string new_str;
    int a;
    cin >> new_str;
    a = stoi(new_str);
    cout << (a+100);
}